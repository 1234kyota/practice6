from api_navi import get_api

def test_get_api():
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
    res = get_api(url = url)

    assert len(res["Products"]) >= 1
    assert res["Products"][0]["Product"]
    assert res["Products"][0]["Product"]["productName"]
    assert res["Products"][0]["Product"]["maxPrice"]
    assert res["Products"][0]["Product"]["minPrice"]
