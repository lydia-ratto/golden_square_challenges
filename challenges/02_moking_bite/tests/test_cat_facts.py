from unittest.mock import Mock
from lib.cat_facts import *

def test_calls_api_to_provide_cat_facts():
    request_facts = Mock(name="requester")
    response_facts = Mock(name="response")
    cat_facts = CatFacts(request_facts)

    request_facts.get.return_value = response_facts
    response_facts.json.return_value = {
        "fact": "Cat fact here"
    }

    assert cat_facts.provide() == "Cat fact: Cat fact here"
