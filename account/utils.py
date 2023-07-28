import requests
from bs4 import BeautifulSoup

def scrape_licence_number_plate(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='item-data')
    if li_elements:
        return li_elements[0].text.strip()