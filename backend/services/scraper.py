from bs4 import BeautifulSoup


def extract_unsubscribe_links(html):
    soup = BeautifulSoup(html, "html.parser") 
    return [
        a['href'] for a in soup.find_all('a',href=True)
        if 'unsubscribe' in a['href'].lower() or 'unsubscribe' in a.text.lower()
    ]

