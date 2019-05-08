import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from typing import List, Dict
import acquire_codeup_blog
import acquire_news_articles

def acquire_articles():
    return acquire_codeup_blog.get_blog_articles(), acquire_news_articles.get_news_articles()