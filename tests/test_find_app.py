import pytest
from contextlib import nullcontext as does_not_raise
from src.find_app.find_app import FindApp

@pytest.mark.parametrize('app_nm, expected_val, expected_except', [
    ('', None, pytest.raises(FileNotFoundError)), # test empty string
    ('python', '/usr/bin/python', does_not_raise()), # test app found via PATH
    ('notepad', None, pytest.raises(FileNotFoundError)), # test app not found via PATH
    ('locate', '/usr/bin/locate', does_not_raise()), # test app found via which
    ('notepad', None, pytest.raises(FileNotFoundError)), # test app not found via which
    ('locate', '/usr/bin/locate', does_not_raise()), # test app found via locate
    ('notepad', None, pytest.raises(FileNotFoundError)), # test app not found via locate
    ('find', '/usr/bin/find', does_not_raise()), # test app found via brute force
    ('notepad', None, pytest.raises(FileNotFoundError)), # test app not found via brute force
])

def test_find(app_nm, expected_val, expected_except):
    with expected_except:
        assert FindApp.find(app_nm) == expected_val