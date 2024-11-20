"""Main Streamlit application for converting sketches to Mermaid diagrams."""

import logging
import time
import streamlit as st
from PIL import Image
from utils import process_image_with_openai, apply_style_to_mermaid, DiagramDraft
from prompts.draft import DRAFT_PROMPT
from prompts.style import STYLE_GUIDE, STYLE_PROMPT
from components.mermaid_viewer import render_mermaid

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


def load_image(image_file):
    """Load and validate uploaded image"""
    try:
        return Image.open(image_file)
    except Exception as e:
        logger.error(f"Failed to load image: {str(e)}")
        st.error(f"Error loading image: {str(e)}")
        return None


def reset_generation_state():
    """Reset all generation-related session state variables"""
    logger.info("Resetting generation state - new image uploaded")
    st.session_state.generation_completed = False
    st.session_state.draft_result = None
    st.session_state.styled_code = None
    st.session_state.processing = False


def main():
    st.set_page_config(
        page_title="Sketch to Professional Visual Converter",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    # Initialize session states
    if "generation_completed" not in st.session_state:
        st.session_state.generation_completed = False
    if "draft_result" not in st.session_state:
        st.session_state.draft_result = None
    if "styled_code" not in st.session_state:
        st.session_state.styled_code = None
    if "processing" not in st.session_state:
        st.session_state.processing = False
    if "last_uploaded_file" not in st.session_state:
        st.session_state.last_uploaded_file = None

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

    # Upload Section
    with st.container():
        st.subheader("Upload Sketch")
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=["png", "jpg", "jpeg"],
            help="Supported formats: PNG, JPEG",
        )

        # Reset state if a new file is uploaded
        if uploaded_file != st.session_state.last_uploaded_file:
            reset_generation_state()
            st.session_state.last_uploaded_file = uploaded_file

        if uploaded_file is not None:
            image = load_image(uploaded_file)
            if image is None:
                logger.warning("Invalid image file uploaded")
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

            # Processing logic
            if generate_button:
                logger.info("Starting diagram processing")
                st.session_state.processing = True

                if st.session_state.processing:
                    try:
                        with st.spinner("Converting your sketch to Mermaid diagram..."):
                            start_time = time.time()

                            # Get structured draft result
                            draft_result = process_image_with_openai(
                                uploaded_file, DRAFT_PROMPT
                            )
                            st.session_state.draft_result = draft_result

                            # Apply styling to the draft code
                            styled_code = apply_style_to_mermaid(
                                draft_result.code,
                                prompt=STYLE_PROMPT,
                                guide=STYLE_GUIDE,
                            )
                            st.session_state.styled_code = styled_code

                            processing_time = time.time() - start_time
                            logger.info(
                                f"Generation completed successfully in {processing_time:.2f}s"
                            )

                            st.session_state.generation_completed = True
                            st.session_state.processing = False

                            # Success message with AI analysis
                            st.success("✨ Diagram generated successfully!")
                            analysis_col1, analysis_col2 = st.columns([1, 3])

                            with analysis_col1:
                                st.caption("AI SUGGESTED TYPE")
                                st.markdown(f"**{draft_result.chart_type.upper()}**")

                            with analysis_col2:
                                st.caption("AI REASONING")
                                st.markdown(draft_result.reason)

                            st.markdown("")

                    except Exception as e:
                        logger.error(f"Diagram generation failed: {str(e)}")
                        st.error(
                            "⚠️ Generation failed. The image might be too complex or unclear. Please try again."
                        )
                        st.session_state.processing = False
                        st.session_state.generation_completed = False

            # Download button for mermaid code
            if st.session_state.generation_completed:
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.download_button(
                        type="primary",
                        label="📥 Download chart",
                        data=st.session_state.styled_code,
                        file_name=f"{st.session_state.draft_result.chart_type}_diagram.txt",
                        mime="text/plain",
                        use_container_width=True,
                    )

            # Initialize tabs
            tab1, tab2 = st.tabs(["Diagram view", "Code view"])

            with tab1:
                if st.session_state.generation_completed:
                    render_mermaid(st.session_state.styled_code)
                else:
                    if not st.session_state.processing:
                        st.info(
                            "Upload an image and click 'Generate Mermaid Diagram' to start"
                        )

            with tab2:
                if st.session_state.generation_completed:
                    st.code(st.session_state.styled_code, language="mermaid")
                    st.markdown("")  # Add minimal whitespace


if __name__ == "__main__":
    main()
