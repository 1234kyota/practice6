from api_ranking import get_api

def test_get_api():
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    res = get_api(url = url)

    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]
    assert res["Items"][0]["Item"]["rank"]
    assert res["Items"][0]["Item"]["itemPrice"]
    assert res["Items"][0]["Item"]["itemName"]