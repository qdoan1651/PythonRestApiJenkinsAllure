import requests, json, os

def test_delete_student():
    # Getting student id from file
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    filename = os.path.join(project_path, 'resources/student_id.txt')
    with open(filename, 'r') as infile:
        student_id = infile.read()
    api_url = api_url = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(student_id)

    response = requests.delete(api_url)
    assert response.status_code == 200

    response_json = json.loads(response.text)

    status = response_json['status']
    msg = response_json['msg']

    assert status == "true"
    assert msg == 'Delete  data success'