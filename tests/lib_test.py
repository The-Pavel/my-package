from toto.lib import who_am_i

def test_whoami():
    res = who_am_i()
    assert "Pavel" in res.split()
