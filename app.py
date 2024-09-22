import streamlit as st
from PIL import Image
import easyocr
import re
import tempfile
import os
import json

def extract_text(image_path):
    reader = easyocr.Reader(['en', 'hi'])  # Initialize EasyOCR with English and Hindi
    results = reader.readtext(image_path, detail=0, paragraph=True)
    extracted_text = ' '.join(results)
    return extracted_text

def highlight_keywords(text, keywords):
    for keyword in keywords:
        pattern = re.compile(f'({re.escape(keyword)})', re.IGNORECASE)
        text = pattern.sub(r'<mark>\1</mark>', text)
    return text

def save_as_json(text):
    # Create a dictionary to hold the extracted text
    data = {"extracted_text": text}
    # Convert to JSON
    json_str = json.dumps(data, indent=4)
    return json_str

def save_as_txt(text):
    # Simply return the text for txt
    return text

def main():
    st.set_page_config(page_title="Multi-Language OCR and Search", layout="wide")
    st.title("📄 Multi-Language OCR and Keyword Search")
    st.markdown("""
    This application allows you to upload an image containing text in **Hindi** and **English**, 
    extracts the text using Optical Character Recognition (OCR), and enables keyword search within the extracted text.
    """)

    # Sidebar for image upload
    st.sidebar.header("Upload Image")
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        try:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)

            with st.spinner('Performing OCR...'):
                # Save uploaded file to a temporary location
                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                    tmp_file.write(uploaded_file.getbuffer())
                    tmp_file_path = tmp_file.name

                # Extract text from the image
                text = extract_text(tmp_file_path)

                # Remove the temporary file
                os.remove(tmp_file_path)

            if text:
                st.subheader("📝 Extracted Text")
                st.write(text)

                # Options to download extracted text as JSON or TXT
                st.subheader("💾 Download Extracted Text")
                download_option = st.selectbox("Choose file format:", ["JSON", "TXT"])

                if download_option == "JSON":
                    json_str = save_as_json(text)
                    st.download_button(
                        label="Download as JSON",
                        data=json_str,
                        file_name="extracted_text.json",
                        mime="application/json"
                    )
                elif download_option == "TXT":
                    txt_str = save_as_txt(text)
                    st.download_button(
                        label="Download as TXT",
                        data=txt_str,
                        file_name="extracted_text.txt",
                        mime="text/plain"
                    )

            else:
                st.warning("No text could be extracted from the image.")

            # Keyword search functionality
            st.subheader("🔍 Keyword Search")
            keywords = st.text_input("Enter keywords separated by commas (e.g., Hello, नमस्ते)")

            if keywords:
                keyword_list = [kw.strip() for kw in keywords.split(",") if kw.strip()]
                if keyword_list:
                    highlighted_text = highlight_keywords(text, keyword_list)
                    st.markdown("**Search Results:**")
                    st.markdown(highlighted_text, unsafe_allow_html=True)
                else:
                    st.warning("Please enter valid keywords separated by commas.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.info("Please upload an image to begin.")

if __name__ == "__main__":
    main()
