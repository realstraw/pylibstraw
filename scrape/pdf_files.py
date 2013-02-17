from bs4 import BeautifulSoup
import re

def get_all_pdfs(html_content):
    """
    return the urls of all pdf files in an html document
    """
    soup = BeautifulSoup(html_content)
    pdf_a = soup.findAll('a', attrs = {
        'href': re.compile(r'^http[s]?://.*?\.pdf$')})
    return [l.get('href') for l in pdf_a]
