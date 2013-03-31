import sys
from pylibstraw.scrape.download_files import get_internet_files
from pylibstraw.scrape.pdf_files import get_all_pdfs

if __name__ == "__main__":
    html_file = sys.argv[1]
    target_location = sys.argv[2]

    with open(html_file, 'r') as html_content:
        pdf_links = get_all_pdfs(html_content)
        get_internet_files(pdf_links, target_location)
