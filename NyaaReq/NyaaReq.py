from lxml import html
from pprint import pprint as print
from os import path
import requests, json, argparse


class NyaaReq():
    def __init__(self):
        self.site = 'https://nyaa.si'
        self.siteQuery = self.site + '/?f={criteria}&c={category}&q={query}'
        with open(path.join(path.dirname(__file__), "types.json"),
                  "rt") as types:
            types = json.load(types)
            self.category = types['category']
            self.criteria = types['criteria']

    def get(self, query, criteria=0, category='0_0', autoparse=True):
        """
        Gets the table of torrents from query site. Returns an lxml Element object if autoparse is False, returns an array containing dictionaries that tells the info of a torrent if autoparse is True. 
        """
        searchHTML = requests.get(
            self.siteQuery.format(criteria=str(criteria),
                                  category=category,
                                  query=query))
        if (status := searchHTML.status_code) >= 400:
            print(f'Error, status code {status}')
            return None
        nyaaPage = html.fromstring(searchHTML.content)
        tableRow = nyaaPage.xpath('//tbody/tr')
        tableData = list()
        for row in tableRow:
            tableData.append(row.findall('td'))
        return tableData if autoparse == False else self.parse(tableData)

    def parse(self, table):
        """
        Parses the table rows (<tr> elements) to get the contents of it. Returns a list containing dictionaries, where a single dictionary contains information for a single torrent. 
        """
        content = list()
        for tableData in table:
            category = tableData[0].find("a").attrib['href'][4:]
            name = tableData[1].find("a").attrib['title']
            url = self.site + tableData[1].find("a").attrib['href']
            torrent = self.site + tableData[2].findall("a")[0].attrib['href']
            magnet = tableData[2].findall("a")[1].attrib['href']
            size = tableData[3].text
            date = tableData[4].text
            seed = tableData[5].text
            leech = tableData[6].text
            downloads = tableData[7].text
            content.append({
                'name': name,
                'url': url,
                'category': self.translate(category),
                'torrent': torrent,
                'magnet': magnet,
                'size': size,
                'date': date,
                'seed': seed,
                'leech': leech,
                'downloads': downloads
            })
        return content

    def translate(self, string):
        """
        Translates nyaa's URL to readable strings
        """
        try:
            return self.category[string]
        except:
            try:
                return self.criteria[string]
            except:
                return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="String to search for in nyaa.si")
    parser.add_argument("--criteria",
                        help="Criteria to search for",
                        nargs='?',
                        default="0")
    parser.add_argument("--category",
                        help="Category to search in",
                        nargs='?',
                        default="0_0")
    args = parser.parse_args()
    nyaa = NyaaReq()
    print(nyaa.get(args.query, args.criteria, args.category), sort_dicts=False)
