import requests, json

def test_verify_added_user():
    # Getting student info from file
    with open('../resources/student_info.json', 'r') as infile:
        expected_data = json.load(infile)

    # Getting student id from file
    with open('../resources/student_id.txt', 'r') as infile:
        student_id = infile.read()
    api_url = api_url = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(student_id)

    response = requests.get(api_url)
    assert response.status_code == 200

    response_json = json.loads(response.text)
    status = response_json['status']
    response_id = response_json['data']['id']
    first_name = response_json['data']['first_name']
    middle_name = response_json['data']['middle_name']
    last_name = response_json['data']['last_name']
    dob = response_json['data']['date_of_birth']

    assert status == "true"
    assert str(response_id) == student_id
    assert first_name == expected_data['first_name']
    assert middle_name == expected_data['middle_name']
    assert last_name == expected_data['last_name']
    assert dob == expected_data['date_of_birth']

# if __name__ == '__main__':
#     filename = '../resources/student_id.txt'
#     with open(filename, 'r') as infile:
#         student_id = infile.read()
#     print(student_id)