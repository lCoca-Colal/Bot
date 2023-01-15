import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import time


def get_first_news():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    
    url = "https://rezka.ag/films/?filter=watching"
    r =requests.get(url=url, headers = headers)
    
    soup = BeautifulSoup(r.text, 'lxml')
    articles_cards = soup.find_all('div', class_='b-content__inline_item')
    
    film_dict ={}
    
    for article in articles_cards:
        articles_title = article.find('div', class_='b-content__inline_item-link').text.strip()
        articles_url = article.find('div', class_='b-content__inline_item-link').a.get('href')
        
        article_id = articles_url.split('/')[-1]
        article_id = article_id[:-5]

        # print(f'{articles_title} | {articles_url}') 
        
        film_dict[article_id] = {
            "articles_title": articles_title,
            "articles_url": articles_url
            
        }
        
    with open("film_dict.json", 'w') as file:
        json.dump(film_dict, file, indent=4, ensure_ascii=False)
        
    # print(film_dict)
        
    
def check_films_update():
    with open("film_dict.json") as file:
        film_dict = json.load(file)
    
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    
    url = "https://rezka.ag/films/?filter=watching"
    r =requests.get(url=url, headers=headers)
    
    soup = BeautifulSoup(r.text, 'lxml')
    articles_cards = soup.find_all('div', class_='b-content__inline_item')
    
    fresh_films = {}
    
    for article in articles_cards:
        articles_url = article.find('div', class_='b-content__inline_item-link').a.get('href')
        
        article_id = url.split('/')[-1]
        article_id = article_id[:-5]
        
        if article_id in film_dict:
            continue
        else:
            articles_title = article.find('div', class_='b-content__inline_item-link').text.strip()
            
            film_dict[article_id] = {
                'articles_title': articles_title,
                'articles_url': articles_url
            
            }

            fresh_films[article_id] = {
                'articles_title': articles_title,
                'articles_url': articles_url
            }
    
    with open("film_dict.json", 'w') as file:
        json.dump(film_dict, file, indent=4, ensure_ascii=False)
        
    return fresh_films

        
def main():
    get_first_news()
    print(check_films_update())
    
if __name__ == '__main__':
    main()