#!/usr/bin/python
# coding: utf8

from typing import Optional

import requests
from .collection import Collection


class Api:
    DIRECTION_ASC = 'asc'
    DIRECTION_DESC = 'desc'

    LISTING_STATE_ACTIVE = 0
    LISTING_STATE_SOLD = 1
    LISTING_STATE_CANCEL = 2

    LISTING_SORT_ID = 'listingId'
    LISTING_SORT_TIME = 'listingTime'
    LISTING_SORT_SALE_TIME = 'saleTime'
    LISTING_SORT_PRICE = 'price'
    LISTING_SORT_RANK = 'rank'

    def __init__(self):
        self.url = 'https://api.ebisusbay.com'

    def get(self, request_url, params={}):
        res = requests.get(self.url + request_url, params).json()
        if res['status'] != 200:
            raise Exception(f"Error {res['status']} : {res['error']}")

        return res

    #####################################
    #                                   #
    #            Collections            #
    #                                   #
    #####################################
    def get_all_collections(self, params: dict = {}) -> list:
        res = self.get('/collectioninfo', params)
        collections = res['collections']
        
        if res['page'] < res['totalPages']:
            params['page'] = res['page'] + 1
            collections += self.get_all_collections(params)

        return collections
    
    def get_collection(self, collection_address: str, params: dict = {}) -> Optional[Collection]:
        params['address'] = collection_address

        res = self.get('/collectioninfo', params)['collections'][0]
        if res:
            return Collection(self, res)

        return None

    def get_collection_floor(self, collection_address: str, params: dict = {}) -> Optional[int]:
        params['collection'] = collection_address
        params['state'] = self.LISTING_STATE_ACTIVE
        params['sortBy'] = self.LISTING_SORT_PRICE
        params['direction'] = self.DIRECTION_ASC
        params['pageSize'] = 1
        params['page'] = 1
        listings = self.get('/listings', params)['listings']

        return int(listings[0]['price']) if len(listings) > 0 else None

    def get_collections(self, params: dict = {}) -> Optional[list]:
        res = self.get('/collectioninfo', params)
        if 'collections' in res:
            return [Collection(self, x) for x in res['collections']]

        return None

    def get_full_collection(self, collection_address: str, params: dict = {}) -> dict:
        params['address'] = collection_address

        return self.get('/fullcollections', params)['nfts']

    #####################################
    #                                   #
    #               Other               #
    #                                   #
    #####################################
    def get_listings(self, params: dict = {}) -> list:
        return self.get('/listings', params)['listings']

    def get_nft(self, collection_address: str, token_id: str) -> dict:
        params = {
            'collection': collection_address,
            'tokenId': token_id
        }
        res = self.get('/nft', params)
        res.pop('status')
        res.pop('error')

        return res

    def get_wallet(self, wallet_address: str, params: dict = {}) -> dict:
        params['wallet'] = wallet_address

        return self.get('/wallets', params)['data']
