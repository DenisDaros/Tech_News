from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    array = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(i["title"], i["url"]) for i in array]


# Requisito 8
def search_by_date(date):
    try:
        dt = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        array = search_news({"timestamp": dt})
        return [(i["title"], i["url"]) for i in array]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    array = search_news({"category": {"$regex": category, "$options": "i"}})
    return [(i["title"], i["url"]) for i in array]
