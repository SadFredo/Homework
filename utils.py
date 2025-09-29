from bs4.element import PageElement


def parse_row(row: PageElement) -> tuple[str, int, int]:
    title = row.find(class_="name -primary prettify").text
    year = row.find(class_="col-releaseyear _aligncenter").text
    rating_element = row.find(class_="rating").get("class")
    rating = rating_element[1].split("-")[1] if len(rating_element) > 1 else None
    return (title, year, rating)

