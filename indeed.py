import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://kr.indeed.com/jobs?q=python&limit=50&radius=25"

def extract_indeed_pages():
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, 'html.parser')
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        # pages.append(link.find("span").string)
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


def extract_indeed_jobs(last_page):
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page * LIMIT}")
        print(result.status_code)