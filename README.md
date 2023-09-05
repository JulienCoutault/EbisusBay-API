# Ebisu's Bay API Wrapper

A Python 3 implementation of the ebisusbay.com REST API.

Ebisu's Bay API docs : https://ebisusbay.readme.io/reference/getting-started

## Installation
```
pip3 install ebisusbay
```

## Simple code
```python
import ebisusbay

api = ebisusbay.Api()
collections = api.get_collections()
```
