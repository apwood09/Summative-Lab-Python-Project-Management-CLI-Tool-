from utils.storage import save_data, load_data
from models.user import User

def test_save_and_load_cycle(tmp_path):
    # temporary file path
    test_file = tmp_path / "test_users.json"
    users = [User("TestBot", "bot@test.com")]
    
    # Logic: Save then immediately Load
    save_data(str(test_file), users)
    loaded_users = load_data(str(test_file), User)
    
    assert len(loaded_users) == 1
    assert loaded_users[0].name == "TestBot"
    assert isinstance(loaded_users[0], User)