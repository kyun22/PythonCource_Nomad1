import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://kr.indeed.com/jobs?q=python&limit=50&radius=25"

def get_last_page():
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, 'html.parser')
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        # pages.append(link.find("company_span").string)
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page

def extract_job(html):
    title = html.find("h2", {"class": "title"}).find('a')['title']
    company_span = html.find("span", {"class": "company"})
    location = html.find("div", {"class": "recJobLoc"})['data-rc-loc']
    job_id = html['data-jk']

    if company_span is None:
        company = "None"
    else:
        if company_span.find("a") is None:
            company = company_span.string
        else:
            company = company_span.find("a").string

    return {
        'from': "Indeed",
        'title': title.strip(),
        'company': company.strip(),
        'location': location.strip(),
        'link': f"https://kr.indeed.com/%EC%B1%84%EC%9A%A9%EB%B3%B4%EA%B8%B0?cmp=%E6%A0%AA%E5%BC%8F%E4%BC%9A%E7%A4%BE%E3%83%8D%E3%82%AF%E3%82%BD%E3%83%B3&t=&jk={job_id}"
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping indeed. {page} page extracting...")
        result = requests.get(f"{URL}&start={page * LIMIT}").text
        soup = BeautifulSoup(result, 'html.parser')
        results = soup.find_all('div', {"class": "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
