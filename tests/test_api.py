#!/usr/bin/python
# coding: utf8

import ebisusbay

from ebisusbay import Api

def setup_api() -> Api:
    api = Api()

    return api


def test_get_collections() -> None:
    api = setup_api()
    res = api.get_collections()

    assert type(res) is list


def test_get_collection() -> None:
    api = setup_api()
    res = api.get_collections()

    assert type(res) is list


def test_get_listings() -> None:
    api = setup_api()
    res = api.get_listings()

    assert type(res) is list
