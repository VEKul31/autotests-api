import pytest
pytest.register_assert_rewrite('fixtures.users')

pytest_plugins = (
    "fixtures.authentication",
    "fixtures.files",
    "fixtures.courses",
    "fixtures.exercises",
    "fixtures.users",
    "fixtures.allure"
)