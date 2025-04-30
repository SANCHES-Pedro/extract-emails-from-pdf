# Extract Emails from PDF

A Python utility that extracts email addresses from PDF documents and saves them to a CSV file.

## Features

- Extract text from PDF documents
- Find all unique email addresses using regex pattern matching
- Export email addresses to a CSV file
- Simple command-line interface

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/extract-emails-from-pdf.git
   cd extract-emails-from-pdf
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Basic usage:

```
python extract_emails_from_pdf.py --pdf_path /path/to/your/document.pdf --output emails.csv
```

### Arguments

- `--pdf_path`: Path to the PDF file (required)
- `--output`: Output CSV file path (optional, default: emails.csv)


## How It Works

1. The script reads the specified PDF document and extracts all text content
2. It uses a regular expression pattern to find email addresses in the extracted text
3. Duplicate email addresses are removed
4. The unique email addresses are saved to a CSV file with a header row

## Output Format

The output CSV file contains a single column with the header "Email" followed by the extracted email addresses:

```
Email
example1@domain.com
example2@domain.com
...
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
