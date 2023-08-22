from core.config.lifespan import load_currencies_from_xml


def test_load_currencies_from_xml():
    currencies = load_currencies_from_xml()
    assert 162 == len(currencies)
