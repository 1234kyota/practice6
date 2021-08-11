import requests
import urllib
import pprint

def get_api(url):
    keyword = input("キーワードを入力してください>>>")
    params = {
    'applicationId':"1008111524082133224",
    'keyword':keyword
    }
    result = requests.get(url, params=params)
    return result.json()

def view_high_and_low(url):
    high_and_low_price_list = get_api(url)
    i = 1
    for item in high_and_low_price_list["Products"]:
        print(f"{i}番目")
        print(item["Product"]["productName"])
        print(item["Product"]["maxPrice"])
        print(item["Product"]["minPrice"])
        i += 1
        print("")

def main():
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
    view_high_and_low(url)


main()
