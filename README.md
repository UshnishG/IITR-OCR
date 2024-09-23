# Multi-Language OCR and Keyword Search Application

## Overview

The **Multi-Language OCR and Keyword Search** application harnesses the power of **Streamlit**, **EasyOCR**, and **PIL** to extract text from images in **Hindi** and **English**. It provides an intuitive interface where users can upload images, perform OCR, search for keywords, and download the results in **JSON** or **TXT** format. This tool is perfect for extracting multilingual content from scanned documents, signs, and more.

---

## 🔥 Key Features

- **Multi-language OCR**: Seamlessly extract text in Hindi and English.
- **Keyword Search & Highlighting**: Easily search for keywords within the extracted text with visual highlights for better clarity.
- **Download Extracted Text**: Get your results in either **JSON** or **TXT** format, making it versatile for different use cases.
- **Interactive & Responsive UI**: A smooth experience using Streamlit for quick, real-time feedback on OCR results.
- **File Format Flexibility**: Supports PNG, JPG, and JPEG image formats for text extraction.
- **Fast Processing**: Leverages EasyOCR for fast and accurate text recognition, even in complex image setups.
  
---

## 🌐 Live Demo

Try out the live demo on Hugging Face Spaces:  
[**OcRecog**](https://huggingface.co/spaces/Ushnish2004/OcRecog)

---

## 💡 Future Updates

- **Support for Additional Languages**: Expanding OCR to recognize more languages.
- **Advanced Text Editing**: Introducing a text editor for modifying extracted text before downloading.
- **Improved Accuracy**: Enhancing keyword search functionality for more precise results.

---

## 🚀 How to Deploy on Hugging Face

1. **Push to GitHub**: Make sure your code is available in a public GitHub repository.
2. **Create a Hugging Face Space**: Choose "Streamlit" as the SDK and link your repository.
3. **Build & Deploy**: After setting up, your app will be live at the provided public URL.

---

## 🛠️ Setup Instructions

### Prerequisites

- **Python** 3.7+
- **pip** for package management

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Set up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

---

## 🔧 Customization

Want to customize the app? Here's what you can modify:

- **Languages Supported**: Modify the `easyocr.Reader` to include more languages.
- **UI Elements**: Use Streamlit's widgets to enhance user interaction, such as sliders, checkboxes, etc.
- **Additional Features**: Add custom functionalities, like extracting specific text regions or applying advanced image preprocessing.

---

## 📞 Contact & Support

Feel free to reach out for any questions, feature requests, or bug reports. Open an issue on the [GitHub repository](https://github.com/UshnishG/IITR-OCR) for prompt support.
