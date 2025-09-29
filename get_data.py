import requests
import bs4
from time import sleep
from typing import Generator

class PagesScrapper:

    base_url = "https://letterboxd.com/%s/films/diary/page/%d"

    def __init__(self, username: str) -> None:
        self.username = username

    def get_page(self, page: int) -> list[bs4.element.PageElement]:
        page_data = requests.get(self.base_url %(self.username, page))
        soup = bs4.BeautifulSoup(page_data.text, "html.parser")
        table = soup.find(id = "diary-table").find("tbody").find_all(class_ = "diary-entry-row")
        return list(table)

    def get_pages(self) -> Generator[list[bs4.element.PageElement]]:
        page_number = 1
        while table:= self.get_page(page_number):
            yield table
            sleep(2)
            page_number += 1
