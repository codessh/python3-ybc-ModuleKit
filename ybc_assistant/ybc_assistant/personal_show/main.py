import json
import requests


class Show:
    """个人秀"""
    def __init__(self, info):
        if 'url' not in info:
            info['url'] = 'http://show.ybccode.com/personal_show/generator'
        self.info = info

    def generate(self):
        data = {
            'user': self.info['user'],
            'gender': self.info['gender'],
            'age': self.info['age'],
            'email': self.info['email'],
            'school': self.info['school'],
            'style': self.info['style'],
            'hobby': self.info['hobby'],
            'intro': self.info['intro'],
        }
        files = [('pic', (self.info['pic'].filename, self.info['pic'].read(), 'image/jpeg'))]
        
        r = requests.post(url=self.info['url'], data=data, files=files)
        return json.loads(r.text)['data']


def generate(info):
    show = Show(info=info)
    return show.generate()
