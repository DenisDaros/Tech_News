from parsel import Selector
import requests
import time

from tech_news.database import create_news


def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    bookmark_list = selector.css("h2.entry-title a::attr(href)").getall()
    return bookmark_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_numbers = selector.css(".next ::attr(href)").get()
    if not (next_page_numbers):
        return None
    return next_page_numbers


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    dict_news = {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "reading_time": int(
            selector.css("li.meta-reading-time::text").get().split(" ")[0]
        ),
        "summary": "".join(
            selector.css(".entry-content > p:first-of-type *::text").getall()
        ).strip(),
        "category": selector.css("div.meta-category span.label::text").get(),
    }
    return dict_news


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    response = []

    html_content_page = fetch(url)
    while len(response) < amount:
        response += scrape_updates(html_content_page)
        html_content_page = fetch(scrape_next_page_link(html_content_page))

    news_content = []
    for i in response[:amount]:
        news_content.append(scrape_news(fetch(i)))
    create_news(news_content)
    return news_content
