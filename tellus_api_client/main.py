import requests

from skimage import io
from io import BytesIO

DOMAIN = "tellusxdp.com"


class TellusApiClient():
    def __init__(self, token: str):
        self.token = token

    def get_blend(self, zoom: int, xtile: int, ytile: int):
        url: str = 'https://gisapi.{}/blend/{}/{}/{}.png'.format(
            DOMAIN, zoom, xtile, ytile)
        headers: dict = {
            "Authorization": "Bearer " + self.token
        }

        r = requests.get(url, headers=headers)
        return io.imread(BytesIO(r.content))
