from datetime import datetime

from src.model.user_model import User


def test_new_user():
    date = datetime.now()
    user = User(id=1, username="jgaray", email="j.garay@uniandes.edu.co", password="afdrfgraafad", salt="asdafeafeaf",
                token="Bearer_adafraf", expireAt=date, createdAt=date)
    assert user.id == 1
    assert user.username == "jgaray"
    assert user.email == "j.garay@uniandes.edu.co"
    assert user.password == "afdrfgraafad"
    assert user.salt == "asdafeafeaf"
    assert user.token == "Bearer_adafraf"
    assert user.expireAt == date
    assert user.createdAt == date
