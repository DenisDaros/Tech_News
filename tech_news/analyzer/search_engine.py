from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    array = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(i["title"], i["url"]) for i in array]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
