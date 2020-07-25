import requests

from skimage import io
from io import BytesIO
from typing import Dict

DOMAIN = "tellusxdp.com"


class TellusApiClient():
    def __init__(self, token: str):
        self.token = token

    def get_blend(self, zoom: int, xtile: int, ytile: int, params: Dict = {}):
        url: str = 'https://gisapi.{}/blend/{}/{}/{}.png'.format(
            DOMAIN, zoom, xtile, ytile)
        headers: dict = {
            "Authorization": "Bearer " + self.token
        }

        r = requests.get(url, headers=headers, params=params)
        return io.imread(BytesIO(r.content))

    def get_osm(self, zoom: int, xtile: int, ytile: int):
        url: str = 'https://gisapi.{}/osm/{}/{}/{}.png'.format(
            DOMAIN, zoom, xtile, ytile)
        headers: dict = {
            "Authorization": "Bearer " + self.token
        }

        r = requests.get(url, headers=headers)
        return io.imread(BytesIO(r.content))
