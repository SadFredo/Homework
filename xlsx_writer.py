from typing import Generator
from openpyxl import Workbook
import config

def write_to_xlsx(
        headers: tuple[None, str, str, str], 
        rows: Generator[tuple[int, str, int, IndentationError]]
    ) -> None:

    wb = Workbook()

    ws = wb.active
    ws.column_dimensions['B'].width = 50
    ws.title = config.TABLE_NAME
    
    ws.append(headers)

    for number, row in enumerate(rows):
        ws.append((number, *row))

    wb.save(config.FILE_PATH)