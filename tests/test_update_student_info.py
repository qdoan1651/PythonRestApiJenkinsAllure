import requests, json

def test_updated_student_info():
    # Getting student info from file
    with open('../resources/updated_student_info.json', 'r') as infile:
        updated_data = json.load(infile)

    # Getting student id from file
    with open('../resources/student_id.txt', 'r') as infile:
        student_id = infile.read()
    api_url = api_url = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(student_id)

    # Add student id to updated_data JSON
    updated_data['id'] = int(student_id)

    response = requests.put(api_url, updated_data)
    assert response.status_code == 200

    response_json = json.loads(response.text)
    status = response_json['status']
    msg = response_json['msg']

    assert status == "true"
    assert msg == 'update  data success'