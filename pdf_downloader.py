import requests
from bs4 import BeautifulSoup
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DOWNLOAD_FOLDER = os.path.join(SCRIPT_DIR, 'downloaded_pdfs')


def download_pdfs_from_url(url, download_folder=DEFAULT_DOWNLOAD_FOLDER):
    print(f"\nProcessing URL: {url}")

    # Define mapping for document types - moved inside to keep it self-contained
    type_mapping = {
        'frq': 'questions',
        'sg': 'scoring_guidelines',
        'apc': 'sample_responses',
        'q\\d': 'sample_responses', # e.g., q1, q2
        'cr-report': 'reports',
        'scoring-statistics': 'reports',
        'score-distributions': 'reports',
        'subscore-score-distributions': 'reports'
    }

    os.makedirs(download_folder, exist_ok=True)

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = []

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.endswith('.pdf'):
            # Handle relative URLs
            if href.startswith('/'):
                pdf_url = requests.compat.urljoin(url, href)
            else:
                pdf_url = href
            pdf_links.append(pdf_url)

    if not pdf_links:
        print(f"No PDF links found on {url}")
        return

    print(f"Found {len(pdf_links)} PDFs. Starting download and organizing...")
    for pdf_url in pdf_links:
        pdf_name = os.path.basename(pdf_url)

        subject = None
        year = None
        doc_type = 'other'

        # Extract subject from URL (more reliable than filename in some cases)
        if 'calculus-ab' in url:
            subject = 'AB'
        elif 'calculus-bc' in url:
            subject = 'BC'

        # Extract year
        year_match = re.search(r'ap(\d{2})-', pdf_name) # Common pattern like ap25-frq
        if year_match:
            year = '20' + year_match.group(1)
        else:
            # Fallback for filenames that might not follow apYY- pattern but contain year
            year_match = re.search(r'(\d{4})', pdf_name) # e.g., 2023
            if year_match:
              year = year_match.group(1)

        # Extract document type
        for key, value in type_mapping.items():
            if re.search(r'\b' + key + r'\b', pdf_name, re.IGNORECASE):
                doc_type = value
                break

        if subject and year:
            destination_dir = os.path.join(download_folder, subject, year, doc_type)
            os.makedirs(destination_dir, exist_ok=True)

            file_path = os.path.join(destination_dir, pdf_name)
            try:
                pdf_response = requests.get(pdf_url, stream=True) # Use stream for large files
                pdf_response.raise_for_status()
                with open(file_path, 'wb') as f:
                    for chunk in pdf_response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Downloaded and organized: '{pdf_name}' to '{destination_dir}'")
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {pdf_url}: {e}")
        else:
            # If subject or year cannot be parsed, download to the base folder
            print(f"Could not fully parse subject or year for '{pdf_name}'. Downloading to base folder.")
            file_path = os.path.join(download_folder, pdf_name)
            try:
                pdf_response = requests.get(pdf_url, stream=True) # Use stream for large files
                pdf_response.raise_for_status()
                with open(file_path, 'wb') as f:
                    for chunk in pdf_response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"Downloaded: '{pdf_name}' to '{download_folder}'")
            except requests.exceptions.RequestException as e:
                print(f"Error downloading {pdf_url}: {e}")

    print(f"Finished processing {url}")

urls_to_process = [
    "https://apcentral.collegeboard.org/courses/ap-calculus-ab/exam/past-exam-questions",
    "https://apcentral.collegeboard.org/courses/ap-calculus-bc/exam/past-exam-questions"
]

for url in urls_to_process:
    download_pdfs_from_url(url)
