import sys
from scrape.download_files import get_internet_files
from pdf_files import get_all_pdfs

if __name__ == "__main__":
    html_file = sys.argv[1]

    pdf_links = get_all_pdfs(html_file)
    get_internet_files(pdf_links)
