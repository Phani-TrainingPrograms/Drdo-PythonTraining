# # What is web scrapping?
'''
Its a way of reading other websites and extract information from it using automation techniques.
It allows programmers to extract data from other web sites. Python is one of the more popular
languages for doing such tasks.
It uses request api to request the data it needs from a web page using HTTP GET. This can also be used to get data from web apis or RESTFull Services.
'''
# Modules required for working with web scrapping
'''
Request Module for making HTTP Requests to the desired web site. 
BeautifulSoup module for python that allows get the data from the desired web page. 

'''
# Example of applying scrapping on some web sites.
import requests
from bs4 import BeautifulSoup
import  pandas as pd

# # Have the page to scrap.
# url = "http://www.bbc.com/news"
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     print("The page is available")
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     headlines = soup.find_all('h2', class_='sc-1207bea1-3 cZBSCm')
#     headlines_list = []
#     for headline in headlines:
#         headlines_list.append(headline.getText())
#
#     df = pd.DataFrame(headlines_list)
#     print(df)
# else:
#     print(f"Failed to get the Page: Status_code: {response.status_code}")

##########################Reading REST API########################
rest_url = 'http://localhost:1234/empList'
rest_response = requests.get(rest_url)
if rest_response.status_code == 200 :
    data = rest_response.json()
    for row in data:
        print(row)


# Etiquettes to be followed while doing web scrapping:
'''
1. API Rate Limiting : When you are accessing web apis, there shall be acertain limit within a 
time frame for allowing anonymous access. 
2. Ethical Scrapping: U may have to check if the website allows scrapping. U can review the 
website's terms of service or its robots.txt file
3. U should be able to handle prominent HTTP errors like 500, 404, 403 etc. 
'''

def scrap_page(url, parser = 'html.parser'):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, parser)
        return soup
    else:
        print(f"Failed to get valid response. Status code : {response.status_code}")
        return None

def scrap_wiki():
    url = "https://en.wikipedia.org/wiki/Web_scraping"
    soup = scrap_page(url)

    if soup:
        title = soup.find('h1', {'id' : 'firstHeading'}).text
        print(f"Title: {title}")

        first_paragraph = soup.find("p").text
        print(f"Content: {first_paragraph}")

def scap_flipkart():
    url = 'https://www.flipkart.com/search?q=Iphone'
    soup = scrap_page(url)
    if soup:
        containers = soup.find_all('div')
    else:
        print("Not available for scrapping")
# scrap_wiki()
scap_flipkart()