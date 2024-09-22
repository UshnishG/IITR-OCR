# Multi-Language OCR and Keyword Search Application

## Overview

This **Multi-Language OCR and Keyword Search** application is built using **Streamlit**, **EasyOCR**, and **PIL** to allow users to extract text from images containing both **Hindi** and **English** languages. After extracting the text, users can search for specific keywords within the extracted text and download the results in **JSON** or **TXT** format.

## Features

- **Multi-language OCR**: Extracts text from images containing both Hindi and English using the EasyOCR library.
- **Keyword Highlighting**: Search for specific keywords within the extracted text, with the matches highlighted for easy identification.
- **Download Options**: Allows users to download the extracted text in **JSON** or **TXT** formats.
- **Streamlit UI**: A simple and interactive user interface for uploading images and interacting with the text extraction process.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

### Setting Up the Environment

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

   Ensure that `requirements.txt` contains the following libraries:
   ```
   streamlit
   easyocr
   pillow
   numpy
   ```
   
### Running the Web Application Locally

1. **Start the Streamlit Application**
   ```bash
   streamlit run app.py
   ```

   Replace `app.py` with the name of your Python file if it's different.

2. **Open in Browser**
   After running the command, Streamlit will provide a local URL (usually `http://localhost:8501`). Open this URL in your web browser to access the application.

## Deployment Process

You can deploy the application using various platforms such as **Streamlit Sharing**, **Heroku**, or **AWS**. Below are brief instructions for deploying on Streamlit Sharing.

### Deploying on Streamlit Sharing

1. **Push to GitHub**
   Make sure your code is pushed to a public GitHub repository.

2. **Sign Up for Streamlit Sharing**
   Go to [Streamlit Sharing](https://share.streamlit.io/) and sign up with your GitHub account.

3. **Deploy the Application**
   - Click on "New app".
   - Select the repository and branch where your application is stored.
   - Enter the path to your main Python file (e.g., `app.py`).
   - Click "Deploy".

4. **Access the Deployed Application**
   After deployment, you’ll receive a public URL where your application is accessible.

### Notes for Deployment

- Ensure that your `requirements.txt` is up to date with all necessary packages.
- If using external APIs or databases, ensure your application can access them securely in the production environment.

## Conclusion

This application allows users to efficiently extract and search for text in images across multiple languages. Feel free to modify and enhance the application as needed. For any issues or feature requests, please open an issue on the GitHub repository.
