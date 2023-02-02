import requests
from bs4 import BeautifulSoup
import csv

details=[]
headers = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70'
        }

def scrap(product):
    for items in product:
        dt={}
        ite=items.find("a",class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
        dt["product_url"]="https://www.amazon.in/"+ite.get("href")
        dt["product_name"]=ite.find("span").contents[0]
        dt["product_price"]=items.find("span",class_="a-price-whole").contents[0]
        dt["rating"]=items.find("span",class_="a-icon-alt").contents[0].split()[0]
        dt["no_of_rating"]=items.find("span",class_="a-size-base s-underline-text").contents[0]
        details.append(dt)
i=1



while i<=2:
        url = f"https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_{i}"
        r = requests.get(url,headers=headers)
        print(r)
        soup = BeautifulSoup(r.content, 'html.parser')
        product=soup.find_all("div" , class_="s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border")
        scrap(product)
        i+=1
        print(len(details))
        
with open('scrapping.csv', 'w' , encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=list(details[0].keys()))
    writer.writeheader()
    writer.writerows(details)