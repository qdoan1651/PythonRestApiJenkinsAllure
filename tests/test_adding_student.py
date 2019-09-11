import requests, json

def test_add_user():
    api_url = api_url = 'http://thetestingworldapi.com/api/studentsDetails'

    request_data = {
        "first_name": "Jason",
        "middle_name": "API",
        "last_name": "Path",
        "date_of_birth": "5-5-1955"
    }

    response = requests.post(api_url, request_data)
    response_json = json.loads(response.text)
    id = response_json['id']; print('ID: {}'.format(id))
    first_name = response_json['first_name']
    middle_name = response_json['middle_name']
    last_name = response_json['last_name']
    dob = response_json['date_of_birth']
    assert response.status_code == 201
    assert first_name == request_data['first_name']
    assert middle_name == request_data['middle_name']
    assert last_name == request_data['last_name']
    assert last_name == request_data['date_of_birth']

