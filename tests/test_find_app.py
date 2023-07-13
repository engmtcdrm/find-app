import pytest
from contextlib import nullcontext as does_not_raise
from src.find_app.find_app import FindApp

@pytest.mark.parametrize('app_nm, orig_val, expected_val, expected_except', [
    ('', '', None, pytest.raise(FileNotFoundError)), # test, empty string
    # create test cases for FindApp.find()

    # test - app name
    ('', '', None, pytest.raises(FileNotFoundError)),

    # test - which, executable
    ('', '', None, pytest.raises(FileNotFoundError)),

    # test - which, not executable
    ('', '', None, pytest.raises(FileNotFoundError)),

    # test - which, not found
    ('', '', None, pytest.raises(FileNotFoundError)),
])

# create test cases for FindApp.find()


#test - app name
def test_app_nm(app_nm, orig_val, expected_val, expected_except):
    with expected_except:
        assert FindApp.find(app_nm) == expected_val

# test - which, executable
def test_which_executable():
    pass

# test - which, not executable
def test_which_not_executable():
    pass

# test - which, not found
def test_which_not_found():
    pass

# test - which, empty string
def test_which_empty_string():
    pass

# test - locate single, executable
def test_locate_single_executable():
    pass

# test - locate single, not executable
def test_locate_single_not_executable():
    pass

# test - locate single, not found
def test_locate_single_not_found():
    pass

# test - locate single, empty string
def test_locate_single_empty_string():
    pass

# test - locate multiple, executable
def test_locate_multiple_executable():
    pass

# test - locate multiple, not executable
def test_locate_multiple_not_executable():
    pass

# test - locate multiple, not found
def test_locate_multiple_not_found():
    pass

# test - locate multiple, empty string
def test_locate_multiple_empty_string():
    pass