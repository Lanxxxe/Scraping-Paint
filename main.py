import requests
from bs4 import BeautifulSoup
import json


base_url = 'https://www.boysen.com.ph/colorcollection/boysen-medley-august-2019'
agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }


def main():
    colorCollections = []
    request = requests.get(base_url, headers=agent)
    soup = BeautifulSoup(request.content, 'html.parser')
    
    colorsContainer = soup.find_all('div', class_='style-module--item--56664')

    for colorsInformation in colorsContainer:
        colors = {}
        palletContainer = colorsInformation.find('div', class_ = 'style-module--itemcolor--25c2b')
        palletCode = colorsInformation.find('div', class_ = 'style-module--itemtitlecode--b7bf0').text.strip()
        palletName = colorsInformation.find('div', class_='style-module--itemtitlename--9451b').text.strip()
        for pallet in palletContainer.children:
            content = pallet.get('style').split(';')
            for pallet in content:
                if ('background-color') in pallet:
                    colorCode = pallet.split(':')[1].strip()
                    colors['rgbCode'] = colorCode

        colors['Code'] = palletCode
        colors['Name'] = palletName
        colorCollections.append(colors)

    with open('colorMedleyCollection.json', 'w') as file:
        json.dump(colorCollections, file, indent=4)

if __name__ == "__main__":
    main()