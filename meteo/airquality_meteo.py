from bs4 import BeautifulSoup


def parse_row(tr):
    cells = list(tr.stripped_strings)
    param = {'code': cells[0], 'name': cells[1], 'description': cells[2], 'altitude': float(cells[3].replace(',', '.'))}
    return param


def read_params():
    with open('DonneesStation.aspx', 'r', encoding='utf8') as reader:
        raw_html = reader.read()
        html = BeautifulSoup(raw_html, 'html.parser')
        rows = [parse_row(row) for row in html.find(id='GridView1').find_all('tr') if row.find('td')]
    return rows


print(read_params())