#!/usr/bin/python
# coding: utf8

from var_dump import var_dump

class Collection:
    api = None
    address = None
    data = {}

    def __init__(self, api, data):
        self.api = api

        if data is str:
            self.address = data
            self.data = {}
        elif isinstance(data, dict):
            self.address = data['address']
            self.data = self.parse_data(data)

    def parse_data(self, data: dict) -> dict:
        to_int = lambda x: int(x)
        to_float = lambda x: float(x)
        actions = {
            'holders': to_int,
            'totalSupply': to_int,
            'active': to_int,
            'complete': to_int,
            'sales': to_int,
            'floorPrice': to_int,
            'avgSalePrice': to_float,
            'volume': to_float,
            'volume1d': to_float,
            'volume1d_increase': to_float,
            'royalty': to_float,
            'sales1d': to_int,
            'sales1d_increase': to_float,
            'avgSalePrice1d': to_float,
            'avgSalePrice1d_increase': to_float,
            'volume7d': to_float,
            'sales7d': to_int,
            'avgSalePrice7d': to_float,
            'volume30d': to_float,
            'sales30d': to_int,
            'avgSalePrice30d': to_float,
        }
        for attr in data:
            if isinstance(data[attr], dict):
                data[attr] = self.parse_data(data[attr])
            elif attr in actions:
                data[attr] = actions[attr](data[attr])

        return data

    def __getattr__(self, attr: str):
        if attr in self.data:
            return self.data[attr]

        return None

    def get_floor(self, params: dict = {}) -> dict:
        return self.api.get_collection_floor(self.address, params)

    def get_listings(self, params: dict = {}) -> list:
        params['collection'] = self.address

        if 'direction' not in params:
            params['direction'] = self.api.DIRECTION_ASC
            params['sortBy'] = self.api.LISTING_SORT_PRICE
        if 'state' not in params:
            params['state'] = self.api.LISTING_STATE_ACTIVE

        var_dump(params)

        return self.api.get_listings(params)
