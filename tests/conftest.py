import pytest
from models.user import User
from models.project import Project

@pytest.fixture
def sample_user():
    return User("Test User", "test@example.com")

@pytest.fixture
def sample_project(sample_user):
    return Project("Test Proj", "Desc", sample_user.id, "2026-01-01")