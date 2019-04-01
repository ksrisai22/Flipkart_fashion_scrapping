import requests
import json
from bs4 import BeautifulSoup
import csv

result_data = []
result_data.append(["image_URL","Neck","Sleeve Style","Sleeve Length","Fit","Pattern","Fabric"])
tshirt_number = 1

for page_number in range(1,10):
    URL = "https://www.flipkart.com/women/tops/pr?sid=2oq%2Cc1r%2Cha6%2Ccck%2C2gs&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&page={}".format(page_number)
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    refined_1 = soup.find_all('div', class_ = "IIdQZO _1R0K0g _1SSAGr")
    for x in refined_1:
        print(x.a.attrs['href'])


    url_list =[]
    for x in refined_1:
      url_list.append(x.a.attrs['href'])


    print("\n--------------------------------------PAGE NO: {} ---------------------------------\n".format(page_number))


    for link in url_list:
        q = requests.get(("https://www.flipkart.com" + link),verify = False)
        product_soup = BeautifulSoup(q.content, 'html.parser')

        # extracting the specifications
        product_name = product_soup.find("span", class_="_35KyD6")

        product_details_keys = product_soup.find_all('div', class_='col col-3-12 _1kyh2f')
        product_details_values = product_soup.find_all('div', class_='col col-9-12 _1BMpvA')

        # Specifications dictionary

        count_attr = 0
        key_list = []
        val_list = []
        for m in product_details_keys[0:9]:
            key_list.append(m.text)
        for m in product_details_values[0:9]:
            val_list.append(m.text)

        # image urls
        img_url = product_soup.find('div',class_ = "_2_AcLJ _3_yGjX")
        try:
            img_url = img_url.attrs["style"][21:-1:]
            img_url = img_url.replace("/128/128/","/800/960/")
        except AttributeError:
             img_url = None
        key_list.append("image_URL")
        val_list.append(img_url)





        # dictionary values
        print(tshirt_number)
        specifications = dict(zip(key_list, val_list))
        #print("\n", json.dumps(specifications,indent =1))
        tshirt_number = tshirt_number + 1

        row = []
        try:
            row.append(specifications["image_URL"])
        except KeyError:
            row.append("null")
        try:
            row.append(specifications["Neck"])
        except KeyError:
            row.append("null")
        try:
            row.append(specifications["Sleeve Style"])
        except KeyError:
            row.append("null")
        try:
            row.append(specifications["Sleeve Length"])
        except KeyError:
            row.append("null")
        try:
            row.append(specifications["Fit"])
        except KeyError:
            row.append("null")
        try:
            row.append(specifications["Pattern"])
        except KeyError:
            row.append("null")
        try:
            row.append(specifications["Fabric"])
        except KeyError:
            row.append("null")

        result_data.append(row)
        

with open('C:\\Users\\1024994\\Desktop\\myntra\\flipkart_code.csv', 'w',newline= '') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(result_data)

csvFile.close()

