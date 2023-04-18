from parsel import Selector
import requests
import time


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
    next_page_numbers = selector.css("div.nav-links a.next::attr(href)").get()
    return next_page_numbers


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
