import requests
import urllib
import pprint

def get_api(url):
    result = requests.get(url)
    return result.json()

def view_item(url):
    item_list = get_api(url)
    i = 1
    for item in item_list["Items"]:
        print(f"{i}番目")
        pprint.pprint(item["Item"]["itemName"])
        pprint.pprint(str(item["Item"]["itemPrice"]) + "円")
        i += 1
        print("")

def main():
    keyword = input("キーワードを入力してください>>>")
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1008111524082133224".format(
        keyword)
    view_item(url)


main()
