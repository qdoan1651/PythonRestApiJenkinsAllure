import requests, json

def test_delete_student():
    # Getting student id from file
    with open('D:/Workspace/Github/RestAPITestingPython/resources/student_id.txt', 'r') as infile:
        student_id = infile.read()
    api_url = api_url = 'http://thetestingworldapi.com/api/studentsDetails/{}'.format(student_id)

    response = requests.delete(api_url)
    assert response.status_code == 200

    response_json = json.loads(response.text)

    status = response_json['status']
    msg = response_json['msg']

    assert status == "true"
    assert msg == 'Delete  data success'