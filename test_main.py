from fastapi.testclient import TestClient
from main import app, students

client = TestClient(app)


def setup_function():
    students.clear()


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_add_student():
    response = client.post(
        "/students",
        json={
            "name": "ANKUSH YADAV",
            "roll_no": "MCA031",
            "marks": 97,
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "ANKUSH YADAV"


def test_invalid_marks():
    response = client.post(
        "/students",
        json={
            "name": "RAGHAV",
            "roll_no": "MCA222",
            "marks": 140,
        },
    )

    assert response.status_code == 422