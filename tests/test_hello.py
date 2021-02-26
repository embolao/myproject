import mylibreria.hello as hello


def test_main(capsys):
    """docstring for test_main"""
    hello.main(['Anthony'])

    out, err = capsys.readouterr()
    assert out == "Hello Sexy Person Anthony\n"
    assert err == ""


def test_main_error_with_empty_string(capsys):
    """docstring for test_main_error_with_empty_string"""
    assert hello.main([''])

    out, err = capsys.readouterr()
    assert out == ''
    assert err == "Person's name must not be empty!\n"
