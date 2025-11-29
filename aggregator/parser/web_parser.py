from bs4 import BeautifulSoup

class WebPageParser:

    @staticmethod
    def parse(html_text):
        soup = BeautifulSoup(html_text, "html.parser")
        table = soup.find("table", {"id": "rates"})
        result = {}
        for row in table.find_all("tr")[1:]:
            cols = row.find_all("td")
            if len(cols) >= 2:
                currency = cols[0].text.strip()
                rate = float(cols[1].text.strip().replace(',', '.'))
                result[currency] = rate
        return result
