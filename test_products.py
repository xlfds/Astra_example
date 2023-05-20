from products.views import get_part_name

def test_get_part_name():
    assert get_part_name({"@name": "Uhlíková tyčka"}) == "Uhlíková tyčka"
    assert get_part_name("Uhlíkiová tyčka") == None
