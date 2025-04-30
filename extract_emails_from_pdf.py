import re
import csv
import argparse
import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

def extract_emails(text):
    """
    Extract email addresses from text using regex
    
    Args:
        text (str): Text to search for emails
        
    Returns:
        list: List of unique email addresses found
    """
    # Regular expression for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    
    # Return unique emails
    return list(set(emails))

def save_to_csv(emails, output_path):
    """
    Save list of emails to a CSV file
    
    Args:
        emails (list): List of email addresses
        output_path (str): Path to save the CSV file
    """
    try:
        with open(output_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Email'])
            for email in emails:
                writer.writerow([email])
        print(f"Successfully saved {len(emails)} emails to {output_path}")
    except Exception as e:
        print(f"Error writing to CSV: {e}")

def main():
    parser = argparse.ArgumentParser(description='Extract emails from a PDF file and save to CSV')
    parser.add_argument('--pdf_path', help='Path to the PDF file')
    parser.add_argument('--output', help='Output CSV file path (default: emails.csv)', default='emails.csv')
    
    args = parser.parse_args()
    
    # Check if PDF file exists
    if not os.path.isfile(args.pdf_path):
        print(f"Error: PDF file '{args.pdf_path}' not found")
        return
    
    # Extract text from PDF
    print(f"Extracting text from {args.pdf_path}...")
    text = extract_text_from_pdf(args.pdf_path)
    
    # Extract emails from text
    print("Finding email addresses...")
    emails = extract_emails(text)
    
    # Save emails to CSV
    print(f"Found {len(emails)} unique email addresses")
    save_to_csv(emails, args.output)

if __name__ == "__main__":
    main()
