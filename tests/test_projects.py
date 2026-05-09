import pytest
from models.project import Project

def test_project_invalid_date():
    """Logic check: Does the Project class reject bad date strings?"""
    with pytest.raises(ValueError) as excinfo:
        Project(
            title="Broken Test",
            description="Testing validation",
            user_id=1,
            due_date="June 1st"  # Bad data
        )
    assert "invalid date" in str(excinfo.value)

def test_project_valid_date():
    """Logic check: Does the Project class accept proper YYYY-MM-DD?"""
    p = Project("Valid", "Desc", 1, "2026-12-31")
    assert p.due_date == "2026-12-31"