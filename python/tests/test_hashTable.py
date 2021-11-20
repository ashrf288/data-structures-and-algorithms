import pytest
from challenges.hashtable.hashTable import HashTable


@pytest.fixture
def hashtable():

    hashtable = HashTable()
    return hashtable


def test_hashtable_contains_bare_value(hashtable):

    hashtable.add("name", "Hamza")
    assert hashtable.contains("name")


def test_hashable_contains_pair_in_a_linked_list(hashtable):

    hashtable.add("name", "Hamza")
    hashtable.add("name", "Alan")
    assert hashtable.contains("name")


def test_hashtable_add(hashtable):

    hashtable.add("name", "Einstein")
    assert hashtable.contains("name")


def test_hashable_add_same_key(hashtable):

    hashtable.add("a", "a")
    hashtable.add("a", "a")
    assert hashtable.contains("a")


@pytest.mark.parametrize(
    "key,hashcode", [("a", 679), ("ab", 341), ("hello", 652), ("something000", 658)]
)
def test_hashtable_hash(key, hashcode, hashtable):

    assert hashtable._HashTable__hash(key) == hashcode


def test_hashtable_get_returns_value(hashtable):

    expected = "Ashrf"
    hashtable.add("name", "Ashrf")
    assert hashtable.get("name") == expected


def test_hashtable_get_returns_correct_last_value(hashtable):

    expected = "Alan"
    hashtable.add("name", "Ashrf")
    hashtable.add("name", "Alan")
    assert hashtable.get("name") == expected


def test_hashtable_get_returns_none_if_key_does_not_exist(hashtable):

    assert not hashtable.get("name")


def test_hashtable_contains_returns_false_if_key_does_not_exist(hashtable):

    assert not hashtable.contains("name")


def test_hashtable_handles_collisions(hashtable):
    expected = "grey"
    hashtable.add("color", "red")
    hashtable.add("color", "blue")
    hashtable.add("color", "grey")
    assert hashtable.get("color") == expected
