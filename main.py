
from indeed import extract_indeed_pages, extract_indeed_jobs




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    last_indeed_page = extract_indeed_pages()
    print(extract_indeed_jobs(last_indeed_page))






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
