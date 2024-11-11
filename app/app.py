# app/app.py
import streamlit as st
from PIL import Image
import io
from utils import process_image_with_openai, apply_style_to_mermaid
from prompts import DRAFT_PROMPT, STYLE_GUIDE
from streamlit_mermaid import st_mermaid


def load_image(image_file):
    """Load and validate uploaded image"""
    try:
        return Image.open(image_file)
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None


def main():
    st.set_page_config(
        page_title="Sketch to Mermaid Converter", page_icon="📊", layout="wide"
    )

    st.title("Sketch to Mermaid.js Converter")
    st.write(
        "Upload a sketch or screenshot of your flowchart to convert it to Mermaid.js code."
    )

    # Initialize session state for storing the generated code
    if "mermaid_code" not in st.session_state:
        st.session_state.mermaid_code = None

    # File uploader
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["png", "jpg", "jpeg"],
        help="Upload a screenshot or sketch of your flowchart",
    )

    # Create two columns for layout
    col1, col2 = st.columns(2)

    if uploaded_file is not None:
        # Load and display the image
        image = load_image(uploaded_file)
        if image:
            with col1:
                st.subheader("Uploaded Image")
                st.image(image, use_container_width=True)

            with col2:
                st.subheader("Generated Mermaid Diagram")
                if st.session_state.mermaid_code:
                    # Render Mermaid diagram using streamlit-mermaid
                    st_mermaid(st.session_state.mermaid_code, height="400px")

                    # Add code display with copy button
                    st.subheader("Mermaid.js Code")
                    st.code(st.session_state.mermaid_code, language="mermaid")

                    # Add download button
                    st.download_button(
                        label="Download Mermaid Code",
                        data=st.session_state.mermaid_code,
                        file_name="flowchart.md",
                        mime="text/plain",
                    )
                else:
                    st.info("Click 'Generate Mermaid Diagram' to process the image")

            # Add processing button
            if st.button("Generate Mermaid Diagram", type="primary"):
                try:
                    with st.spinner("Processing image..."):
                        # Generate draft diagram
                        draft_code = process_image_with_openai(
                            uploaded_file, DRAFT_PROMPT
                        )

                        # Apply styling without sending image again
                        styled_code = apply_style_to_mermaid(draft_code, STYLE_GUIDE)

                        # Store the result
                        st.session_state.mermaid_code = styled_code

                        # Show success message
                        st.success("Diagram generated successfully!")

                        # Rerun to update the display
                        st.rerun()

                except Exception as e:
                    st.error(f"Error generating diagram: {str(e)}")


if __name__ == "__main__":
    main()
