from api import get_api,view_item

def test_get_api():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1008111524082133224".format(
    keyword)
    res = get_api(url = url)

    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]
    assert res["Items"][0]["Item"]["itemName"]
    assert res["Items"][0]["Item"]["itemPrice"]