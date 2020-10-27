from lxml import html
import requests


class NyaaReq():
    def __init__(self):
        self.site = 'https://nyaa.si'
        self.siteQuery = self.site + '/?f={criteria}&c={category}&q={query}'

    def get(self, query, criteria=0, category='0_0'):
        searchHTML = requests.get(
            self.siteQuery.format(criteria=str(criteria),
                                  category=str(category),
                                  query=query))
        if (status := searchHTML.status_code) >= 400:
            print(f'Error, status code {status}')
            return None
        nyaaPage = html.fromstring(searchHTML.content)
        tableRow = nyaaPage.xpath('//tbody/tr')
        tableData = list()
        for row in tableRow:
            tableData.append(row.findall('td'))
        return tableData

    def parse(self, tableRow):
        content = list()
        for tableData in tableRow:
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
            content.append([
                category, name, url, torrent, magnet, size, date, seed, leech,
                downloads
            ])
        return content


if __name__ == "__main__":
    pass
