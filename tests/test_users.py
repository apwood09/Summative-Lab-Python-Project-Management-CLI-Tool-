import pytest
from models.user import User

# successful creation
def test_user_creation():
    """Verify that a User object stores attributes correctly."""
    user = User(name="Alice", email="alice@example.com")
    assert user.name == "Alice"
    assert user.email == "alice@example.com"
    assert hasattr(user, 'id')

# email validation logic
def test_user_invalid_email():
    """Verify the @email.setter raises ValueError for missing '@'."""
    with pytest.raises(ValueError) as excinfo:
        User(name="Bob", email="bob_at_gmail.com")
    
    assert "Invalid email" in str(excinfo.value)

# ID incrementing logic
def test_user_id_increment():
    """Verify that every new user gets a unique, incremented ID."""
    # Reset counter if necessary or just check relative IDs
    u1 = User("User1", "u1@test.com")
    u2 = User("User2", "u2@test.com")
    assert u2.id == u1.id + 1

# loading from dictionary (Persistence logic)
def test_user_from_dict():
    """Simulate loading a user from JSON data using **kwargs."""
    user_data = {
        "name": "Charlie",
        "_email": "charlie@test.com", 
        "id": 99
    }
    user = User(**user_data)
    assert user.name == "Charlie"
    assert user.email == "charlie@test.com"
    assert user.id == 99