"""Main Streamlit application for converting sketches to Mermaid diagrams."""

import streamlit as st
from PIL import Image
from streamlit_mermaid import st_mermaid
from utils import process_image_with_openai, apply_style_to_mermaid
from prompts.draft import DRAFT_PROMPT
from prompts.style import STYLE_GUIDE, STYLE_PROMPT


def load_image(image_file):
    """Load and validate uploaded image"""
    try:
        return Image.open(image_file)
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None


def apply_zoom_to_mermaid(mermaid_code: str, zoom_level: float) -> str:
    """Apply zoom level to Mermaid code by adding initialization directive"""
    init_directive = f"""%%{{init: {{
        "theme": "dark",
        "flowchart": {{
            "curve": "basis",
            "nodeSpacing": {50 * zoom_level},
            "rankSpacing": {50 * zoom_level}
        }}
    }}}}%%\n"""

    if "%%{init:" in mermaid_code:
        import re

        mermaid_code = re.sub(r"%%{init:.*?}%%\n?", "", mermaid_code)

    return init_directive + mermaid_code


def main():
    st.set_page_config(
        page_title="Sketch to Professional Visual Converter",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Initialize session state
    if "generation_completed" not in st.session_state:
        st.session_state.generation_completed = False
    if "zoom_level" not in st.session_state:
        st.session_state.zoom_level = 1.0
    if "base_mermaid_code" not in st.session_state:
        st.session_state.base_mermaid_code = None
    if "processing" not in st.session_state:
        st.session_state.processing = False

    # Header Section
    left_spacer, center_col, right_spacer = st.columns([2, 6, 2])

    with center_col:
        st.title("Sketch to Visual Converter")
        st.write(
            "Transform your sketches into professional diagrams with AI and Mermaid.js."
        )

    # Simple step guide with centered layout
    spacer1, col1, col2, col3, spacer2 = st.columns([2, 2, 2, 2, 2])

    with col1:
        st.caption("1️⃣ Upload your sketch")
        st.markdown("Take a photo or screenshot of your hand-written diagram sketch")
    with col2:
        st.caption("2️⃣ Generate diagram")
        st.markdown(
            "Click generate button and wait for generation of mermaid visual diagram"
        )
    with col3:
        st.caption("3️⃣ Explore & export")
        st.markdown("Explore visual by zooming in or out and download code if desired")

    st.markdown("---")

    # Upload Section - Updated help text
    with st.container():
        st.subheader("Upload Sketch")
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=["png", "jpg", "jpeg"],
            help="Supported formats: PNG, JPEG",  # More generic help text
        )
        if uploaded_file is not None:
            image = load_image(uploaded_file)
            if image is None:
                st.error(
                    "Unable to process image. Please ensure it's a valid PNG or JPEG file."
                )
                generate_button = st.button("Generate Mermaid Diagram", disabled=True)
            else:
                generate_button = st.button(
                    "Generate Mermaid Diagram",
                    type="primary",
                    use_container_width=False,
                )
        else:
            generate_button = st.button("Generate Mermaid Diagram", disabled=True)

    st.markdown("---")

    # Main content area
    if uploaded_file is not None and image is not None:
        left_col, right_col = st.columns([1, 1], gap="large")

        with left_col:
            st.subheader("Original Image")
            st.markdown("")
            if image:
                st.image(image, use_container_width=True, width=600)

        with right_col:
            st.subheader("Generated Diagram")
            st.markdown("")

            # Processing logic - Updated messages
            if generate_button:
                st.session_state.processing = True

            if st.session_state.processing:
                try:
                    with st.spinner("Converting your sketch to Mermaid diagram..."):
                        draft_code = process_image_with_openai(
                            uploaded_file, DRAFT_PROMPT
                        )
                        styled_code = apply_style_to_mermaid(
                            draft_code, prompt=STYLE_PROMPT, guide=STYLE_GUIDE
                        )
                        st.session_state.base_mermaid_code = styled_code
                        st.session_state.generation_completed = True
                        st.session_state.processing = False
                        st.success(
                            "✨ Diagram generated! Use the toolbar below to adjust the view. Use the code view to download the mermaid code."
                        )
                except Exception as e:
                    print(e)
                    st.error(
                        "⚠️ Generation failed. The image might be too complex or unclear. Please try again."
                    )
                    st.session_state.processing = False
                    st.session_state.generation_completed = False

            # Initialize tabs
            tab1, tab2 = st.tabs(["Diagram view", "Code view"])

            with tab1:
                if st.session_state.generation_completed:
                    cols = st.columns([1, 1, 1, 10])

                    with cols[0]:
                        if st.button("➕", help="Increase diagram size"):
                            st.session_state.zoom_level = min(
                                2.5, st.session_state.zoom_level + 0.5
                            )

                    with cols[1]:
                        if st.button("➖", help="Decrease diagram size"):
                            st.session_state.zoom_level = max(
                                0.5, st.session_state.zoom_level - 0.5
                            )

                    with cols[2]:
                        if st.button("⟲", help="Reset diagram size"):
                            st.session_state.zoom_level = 1.0

                    zoomed_code = apply_zoom_to_mermaid(
                        st.session_state.base_mermaid_code, st.session_state.zoom_level
                    )
                    st_mermaid(zoomed_code, height="700px")

                else:
                    if not st.session_state.processing:
                        st.info(
                            "Upload an image and click 'Generate Mermaid Diagram' to start"
                        )

            with tab2:
                if st.session_state.generation_completed:
                    st.code(st.session_state.base_mermaid_code, language="mermaid")
                    st.markdown("")  # Add minimal whitespace
                    st.download_button(
                        label="Download Mermaid code",
                        data=st.session_state.base_mermaid_code,
                        file_name="flowchart.txt",
                        mime="text/plain",
                    )


if __name__ == "__main__":
    main()
