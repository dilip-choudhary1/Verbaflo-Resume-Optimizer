# LinkedIn PDF to HTML Resume Generator

## Description
This web application allows you to upload a LinkedIn PDF resume and convert it into an HTML resume using OpenAI's GPT-3 model. The application also provides options for customizing the content and downloading the final resume as an HTML file.

## Features
- Parse LinkedIn PDFs to extract resume details.
- Customize which sections (Experience, Education, Skills, etc.) appear in the resume.
- Generate a clean, HTML-formatted resume.
- Download the HTML resume.
- Live resume preview.
- Different resume themes.
- Editable resume content.

## Tech Stack
- Streamlit for the frontend UI.
- PyMuPDF for extracting text from PDFs.
- OpenAI API for content generation.
- BeautifulSoup for formatting HTML.

## Instructions
1. Clone the repository.
2. Install the required libraries.
3. Set your OpenAI API key in Streamlit secrets.
4. Deploy the application using Vercel or GitHub Pages.
5. Upload your LinkedIn PDF and generate your resume.

## Install dependencies:
pip install -r requirements.txt

## Run the Streamlit application:
streamlit run app.py

Open the application in your browser at http://localhost:8501


