import json
import requests


class Profile:
    """形象大师"""
    def __init__(self, info):
        if 'url' not in info:
            info['url'] = 'http://show.ybccode.com/image_master/download'
        self.info = info

    def generate(self):
        data = self.info
        r = requests.post(url=self.info['url'], data=data)
        return json.loads(r.text)['data']


def generate(info):
    show = Profile(info=info)
    return show.generate()
