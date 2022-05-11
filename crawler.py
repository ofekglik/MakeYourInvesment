from bs4 import BeautifulSoup
import requests
import time
from ProvidentFund import *


class Crawler:

    def __init__(self):
        self.provident_funds = []
        pass


    def scrape_gemel(self):
        url = "https://www.mygemel.net/%D7%A7%D7%95%D7%A4%D7%AA-%D7%92%D7%9E%D7%9C-%D7%9C%D7%94%D7%A9%D7%A7%D7%A2%D7%94"
        website_request = requests.get(url)
        website_content = BeautifulSoup(website_request.content, 'html.parser')
        all_tables = website_content.find_all("table")
        for table in all_tables:
            prov_funds = table.findAll('tr')[1:-1]
            for fund in prov_funds:

                title = fund.parent.parent.find('h2').text
                finder = fund.find('td').find('a', href = True)
                name = finder.text
                url = str(finder['href'])
                provident_fund = ProvidentFund(title, name, url)
                self.provident_funds.append(provident_fund)








    def scrape_provident_fund(self):
        for prov_fund in self.provident_funds:
            url = prov_fund.get_url()
            website_request = requests.get(url)
            website_content = BeautifulSoup(website_request.content, 'html.parser')
            ull = website_content.findAll('ul', class_='mr-4')

            for index in range(len(ull)-1):
                ul = ull[index]
                text = ul.contents[1].text
                if "תשואה" in text:
                    all_li = ul.findAll('li')
                    # for index in range(len(all_li)-1):
                    #     li = all_li[index]
                    #
                    #     ratio = float(li.text.split(':')[1].strip().replace('%', ''))
                    #     if index == 0:
                    #         prov_fund.set_current_month_yield(ratio)
                    #     elif index == 1:
                    #         prov_fund.set_current_year_yield(ratio)
                    #     elif index == 2:
                    #         prov_fund.set_annual_yield(ratio)
                    #     elif index == 3:
                    #         prov_fund.set_biannual_yield(ratio)
                break

        print()








c1 = Crawler()
c1.scrape_gemel()
c1.scrape_provident_fund()


