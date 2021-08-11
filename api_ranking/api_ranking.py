import requests
import urllib
import pprint
import pandas as pd

def get_api(url):
    keyword = input("ジャンルIDを入力してください>>>")
    params = {
    'applicationId':"1008111524082133224",
    'genreId':keyword,
    }
    result = requests.get(url, params=params)
    return result.json()

def view_ranking(url):
    ranking_list = get_api(url)
    ranking_to_csv = []
    for item in ranking_list["Items"]:
        list = [item["Item"]["rank"],item["Item"]["itemName"],item["Item"]["itemPrice"]]
        ranking_to_csv.append(list)
    df = pd.DataFrame(ranking_to_csv,columns=["Rank","Name","Price"])
    df.to_csv("./api_ranking.csv", index=False)

def main():
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    view_ranking(url)

main()
