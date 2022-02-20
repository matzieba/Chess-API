from classes import King
import requests as r

import os
import tempfile

import pytest
import main


@pytest.fixture
def client():
    db_fd, main.app.config["DATABASE"] = tempfile.mkstemp()
    main.app.config["TESTING"] = True

    with main.app.test_client() as client:
        with main.app.app_context():
            main.init_db()
        yield client

    os.close(db_fd)
    os.unlink(main.app.config["DATABASE"])


class TestClassClass:
    def test_one(self):
        king = King("A1")
        assert king.list_available_moves() == ["A2", "B2", "B1"]

    def test_two(self):
        king = King("A20")
        assert pytest.raises(ValueError)

    def test_three(self):
        king = King("a6")
        assert pytest.raises(ValueError)


class TestClassApiMoves:
    def test_one(self):
        url = "http://127.0.0.1:5000//api/v1/bla_bla/A7"
        resposne = r.get(url)
        assert resposne.status_code == 404

    def test_two(self):
        url = "http://127.0.0.1:5000//api/v1/queen/A7"
        resposne = r.get(url)
        assert resposne.status_code == 200

    def test_three(self):
        url = "http://127.0.0.1:5000//api/v1/queen/A17"
        resposne = r.get(url)
        assert resposne.status_code == 409


class TestClassApiValid:
    def test_one(self):
        url = "http://127.0.0.1:5000//api/v1/queen/A7/A50"
        resposne = r.get(url)
        data = resposne.json()
        assert data["MoveValid"] == "Move is invalid"

    def test_two(self):
        url = "http://127.0.0.1:5000//api/v1/bla_bla/A7/A50"
        resposne = r.get(url)
        data = resposne.json()
        assert pytest.raises(KeyError)

    def test_three(self):
        url = "http://127.0.0.1:5000//api/v1/pawn/A7/B7"
        resposne = r.get(url)
        data = resposne.json()
        assert data["MoveValid"] == "Move is valid"
