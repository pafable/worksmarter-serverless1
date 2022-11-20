import json
import ssl
from urllib import request

ssl._create_default_https_context = ssl._create_unverified_context
URL = "https://api.coindesk.com/v1/bpi/currentprice.json"

class Price:
    def __init__(self, url):
        self.url = url

    def get_usd(self):
        resp = request.urlopen(self.url)
        resp_str = resp.read().decode()
        resp_json = json.loads(resp_str)
        return round(resp_json["bpi"]["USD"]["rate_float"], 2)

def xyz_handler(event, context):
    # URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
    # resp = request.urlopen(URL)
    # resp_str = resp.read().decode()
    # resp_json = json.loads(resp_str)
    #
    # usd = resp_json["bpi"]["USD"]["rate_float"]
    # gbp = resp_json["bpi"]["GBP"]["rate_float"]
    # eur = resp_json["bpi"]["EUR"]["rate_float"]
    # print(f"USD: {round(usd, 2)}")
    # print(f"GBP: {round(gbp, 2)}")
    # print(f"EUR: {round(eur, 2)}")
    btc_usd = Price(URL)
    print(btc_usd.get_usd())


# execution from console
if __name__ == "__main__":
    btc = Price(URL)
    print(btc.get_usd())
