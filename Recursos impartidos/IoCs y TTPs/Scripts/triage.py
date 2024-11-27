#@creator Ivan Portillo & Claudia Sánchez-Girón - XVIII Jornadas STIC CCN-CERT
# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

def search_triage(keyword):
	
    url = 'https://tria.ge/s?q=family:'+ keyword
    sha256_hashList = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    html_text = soup.find_all("button", class_="button primary icon")
    print("*) Hashes en SHA256 extraidos de tria.ge sobre la familia: "+keyword)
    for hash in html_text:
        if hash['data-clipboard'] not in sha256_hashList:
            sha256_hashList.append(hash['data-clipboard'])
            print(hash['data-clipboard'])

if __name__ == '__main__':
    keyword='ransomhub'
    search_triage(keyword)