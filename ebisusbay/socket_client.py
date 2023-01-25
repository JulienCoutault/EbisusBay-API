#!/usr/bin/python
# coding: utf8

import socketio

import json
from functools import *

class SocketClient():
    def __init__(self, debug: bool = True):
        self.url    = 'wss://api.ebisusbay.com'
        self.sio    = socketio.Client()
        self.debug  = debug
        self.events = {}

        self.sio.on('connect', lambda: self.on_connect())
        self.sio.on('*', lambda message, data: self.on_all(message, data))

    def connect(self):
        self.sio.connect(self.url)

    def disconnect(self):
        self.sio.disconnect()

    def on_all(self, message, data):
        if self.debug:
            print(f"Message `{message}`")
        if message in self.events.keys():
            data = json.loads(data)
            for func in self.events[message]:
                func(data)

    def on_connect(self):
        print("Connected!")

    def on_connect_error(self):
        print("The connection failed!")

    def on_disconnect(self):
        print("Disconnected!")

    def add_event(self, message: str, func) -> None:
        if message not in self.events.keys():
            self.events[message] = []
            
        self.events[message].append(func)

    def set_event(self, message: str, func) -> None:
        self.events[message] = [func]

