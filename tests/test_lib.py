from bbquoteptmelb.lib import get_quote

def test_type_get_quote():
    assert type(get_quote()) == str

def test_len_get_quote():
    assert len(get_quote()) > 0
