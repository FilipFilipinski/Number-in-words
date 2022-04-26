import requests
import json


def tests():
    link = 'http://127.0.0.1:5000/api/'
    assert json.loads(requests.get(link + '12').content) == {'12': 'twelve'}
    print(json.loads(requests.get(link + '12a').content))
    assert json.loads(requests.get(link + '12a').content) == {'message': 'Bad Request', 'status': 400}
    assert json.loads(requests.get(link + '10').content) == {'10': 'ten'}
    assert json.loads(requests.get(link + 'test').content) == {'message': 'Bad Request', 'status': 400}
    assert json.loads(requests.get(link + '-1').content) == {'message': 'Bad Request', 'status': 400}

    print('APPA hop hop, tests passed ❤️')


tests()
