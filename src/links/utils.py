from bs4 import BeautifulSoup
import requests



import requests
import lxml
from bs4 import BeautifulSoup

# def getLinkData(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36",
#         "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
#     }
#
#     response = requests.get(url, headers=headers)
#
#     soup = BeautifulSoup(response.text, "lxml")
#
#     name = soup.select_one(selector="#productTitle").getText()
#     name = name.strip()
#
#     price = soup.select_one(selector="#priceblock_ourprice").getText()
#     price = float(price[1:])
#
#     return name, price




#url = input("Enter url\n")

def get_link_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76'
                      ' Safari/537.36', "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,"
                  "application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate"}
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.text, 'lxml')

    if (url.__contains__("www.flipkart.com")):
        print("Product is from flipkart")
        price = soup.find('div', {'class', '_30jeq3 _16Jk6d'}).text[1:]
        # price = soup.select_one("._30jeq3 _16Jk6d")
        name = soup.find('span', {'class', 'B_NuCI'})
        # print("Price of "+name.text+" is "+price.text)
    elif (url.__contains__("www.amazon.in")):
        print("Product is from amazon")
        price = soup.find('span', {'class', 'a-offscreen'}).text[1:]
        name = soup.find('span', {'class', 'a-size-large product-title-word-break'})

    return name.text,float(price)
