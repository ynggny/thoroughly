import requests
import csv
from bs4 import BeautifulSoup

data = []

with open("英単語.csv","r") as f:
    reader = csv.reader(f)

    for row in reader:
        data.extend(row)
panty = []
for i in data:
    targett_url = 'https://ejje.weblio.jp/content/'
    target_url = targett_url + i
    r = requests.get(target_url)         #requestsを使って、webから取得
    soup = BeautifulSoup(r.text, 'lxml') #要素を抽出
    for a in soup.find_all(class_="content-explanation ej"):
      panty.extend(a)
      with open('日本語訳.csv', 'w') as file:
          writer = csv.writer(file, lineterminator='\n')
          writer.writerow(panty)
          print("done")
