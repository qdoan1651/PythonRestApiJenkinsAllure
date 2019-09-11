import requests, json

def test_verify_added_user():
    id = '144865'
    api_url = api_url = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(id)

    request_data = {
        "first_name": "Jason",
        "middle_name": "API",
        "last_name": "Path",
        "date_of_birth": "5-5-1955"
    }

    response = requests.get(api_url)
    assert response.status_code == 200
    # print(response.text)
    response_json = json.loads(response.text)
    status = response_json['status']
    response_id = response_json['data']['id']
    first_name = response_json['data']['first_name']
    middle_name = response_json['data']['middle_name']
    last_name = response_json['data']['last_name']
    dob = response_json['data']['date_of_birth']

    assert status == "true"
    assert str(response_id) == id
    assert first_name == request_data['first_name']
    assert middle_name == request_data['middle_name']
    assert last_name == request_data['last_name']
    assert dob == request_data['date_of_birth']