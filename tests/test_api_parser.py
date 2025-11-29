from aggregator.parsers.api_parser import APIParser

def test_parse_api():
    fake_json = {"rates": {"USD": 1.2, "EUR": 0.95}}
    parsed = APIParser.parse(fake_json)
    assert parsed["USD"] == 1.2
    assert parsed["EUR"] == 0.95
