import pytest
from pymongo import MongoClient
# from appweb.app_flask import app
# revoir je sais plus ce que on avait fais 

# @pytest.fixture()
# def app2():
#     app.config.update({
#         "TESTING": True,
#     })
#     yield app


@pytest.fixture()
def mongo_connection():
    try:
        client = MongoClient()
        return client
    except Exception:
        pytest.fail("connextion echec")

def test_mongo_db(mongo_connection):
    try:
        mongo_connection.quote_db
    except Exception:
        pytest.fail("connextion echec")
