import config
from get_data import PagesScrapper
from utils import parse_row
from xlsx_writer import write_to_xlsx

def main() -> None:
    result_table = [
        parse_row(row)
        for table in PagesScrapper(config.USERNAME).get_pages()
        for row in table
    ]
    headers = (None, "film_name", "year", "rating") 
    write_to_xlsx(headers, result_table)
    print("Готово!")
    

if __name__ == "__main__":
    main()