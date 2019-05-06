import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from typing import List, Dict

sections = ['business', 'sports', 'technology', 'entertainment']

def article_dict(soup):
    return {
        'title': soup.find(class_='news-card-title').find('a').text.strip(),
        'content': (soup.find(class_='news-card-content')
                    .find('div', attrs={'itemprop': 'articleBody'})
                    .text.strip())
    }

def get_section(section):
    url = f'https://inshorts.com/en/read/{section}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    articles = [article_dict(article) for article in soup.find_all(class_='news-card')]
    for article in articles:
        article['category'] = section
    return articles

def get_news_articles():
    allsections = [get_section(section) for section in sections]
    return allsections
