import urllib
import os
import time

from pushover import Client

from pyquery import PyQuery as pq


def parse_pollen_count(domain):
    pyquery_parser = pq(url=domain,
                        opener=lambda url: urllib.urlopen(url).read())
    return pyquery_parser(".pollen-num").html()


def get_daily_pollen():
    return parse_pollen_count("http://www.atlantaallergy.com/")


def get_pushover_client():
    api_key = os.environ.get("ATL_ALLERGY_PUSHOVER_API")
    user_key = os.environ.get("PUSHOVER_USER_KEY")
    return Client(user_key, api_token=api_key)


def pushover_allergy_count(pushover_client, pollen_count):
    title = "Pollen Count for " + time.strftime("%x")
    message = "The pollen count for today is " + pollen_count + "."

    pushover_client.send_message(message, title=title)


if __name__ == "__main__":
    pushover_client = get_pushover_client()
    pollen_count = get_daily_pollen()
    if int(pollen_count) > 100:
        pushover_allergy_count(pushover_client, pollen_count)
