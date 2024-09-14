import streamlit as st
import fitz  # PyMuPDF
import openai
import html2text
from bs4 import BeautifulSoup
from io import BytesIO
# Set the OpenAI API key
openai.api_key = st.secrets["general"]["openai_api_key"]

# Function to extract text from LinkedIn PDF
def extract_text_from_pdf(pdf_file):
    # Read the uploaded PDF file as bytes
    pdf_bytes = pdf_file.read()
    
    # Check if the file is empty
    if not pdf_bytes:
        st.error("The uploaded PDF file is empty.")
        return ""
    
    # Open the file as a document
    try:
        doc = fitz.open(stream=BytesIO(pdf_bytes), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        return ""
    
    


# Function to interact with OpenAI API for resume generation
def generate_resume_from_text(extracted_text, sections):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the newer model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Generate an HTML resume using this extracted text: {extracted_text}"},
            ],
            max_tokens=2000,
        )
        resume_html = response['choices'][0]['message']['content']
        return resume_html
    except Exception as e:
        st.error(f"Error generating resume: {e}")
        return ""

# Function to clean and prettify HTML
def prettify_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.prettify()

# Main Streamlit App
def main():
    st.title("LinkedIn PDF to HTML Resume Converter")
    
    # PDF Upload
    pdf_file = st.file_uploader("Upload LinkedIn PDF", type=["pdf"])
    
    # Section selection
    st.write("Select the sections to include in your resume:")
    sections = st.multiselect("Sections", ['Experience', 'Education', 'Skills', 'Projects', 'Certifications', 'Summary'])
    
    if pdf_file is not None:
        st.write("Processing your PDF...")
        
        # Extract text from the uploaded PDF
        extracted_text = extract_text_from_pdf(pdf_file)
        
        if extracted_text:
            # Display extracted text from PDF
            st.write("Extracted text from the PDF:")
            st.text(extracted_text)
        else:
            st.error("Failed to extract text from the PDF.")
    
    # Display HTML resume
    if pdf_file and sections:
        # Extract text from PDF
        extracted_text = extract_text_from_pdf(pdf_file)
        st.subheader("Extracted Text:")
        st.write(extracted_text)
        
        # Generate HTML resume
        html_resume = generate_resume_from_text(extracted_text, ', '.join(sections))
        cleaned_html = prettify_html(html_resume)
        
        # Display generated resume
        st.subheader("Generated HTML Resume")
        st.markdown(cleaned_html, unsafe_allow_html=True)
        
        # Download HTML file option
        st.download_button(label="Download HTML Resume", data=cleaned_html, file_name="resume.html", mime="text/html")

if __name__ == "__main__":
    main()
