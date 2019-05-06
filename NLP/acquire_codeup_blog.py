import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_article1():
    url = 'https://codeup.com/codeups-data-science-career-accelerator-is-here/'
    headers = {'User-Agent':'Codeup Ada Data Science'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article1_content = soup.find(class_ = 'mk-single-content').text
    return dict(title='Codeup Data Science Career Accelerator Is Here', content=article1_content)

def get_article2():
    url = 'https://codeup.com/data-science-myths/'
    headers = {'User-Agent':'Codeup Ada Data Science'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article2_content = soup.find(class_ = 'mk-single-content').text
    article2_content = article2_content[:4312]
    return dict(title='Codeup Ada Data Science', content=article2_content)

def get_article3():
    url = 'https://codeup.com/data-science-vs-data-analytics-whats-the-difference/'
    headers = {'User-Agent':'Codeup Ada Data Science'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article3_content = soup.find(class_ = 'mk-single-content').text
    return dict(title='Data Science vs Data Analytics. What\'s the difference?', content=article3_content)

def get_article4():
    url = 'https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/'
    headers = {'User-Agent':'Codeup Ada Data Science'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article4_content = soup.find(class_ = 'mk-single-content').text
    return dict(title='10 Tips to Crush It at The SA Tech Job Fair', content=article4_content)

def get_article5():
    url = 'https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/'
    headers = {'User-Agent':'Codeup Ada Data Science'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    article5_content = soup.find(class_ = 'mk-single-content').text
    return dict(title='Competitor Bootcamps are closing. Is the model in danger?', content=article5_content)

def get_blog_articles(): 
    blog_articles = []
    blog_articles.append(get_article1())
    blog_articles.append(get_article2())
    blog_articles.append(get_article3())
    blog_articles.append(get_article4())
    blog_articles.append(get_article5())
    return blog_articles

