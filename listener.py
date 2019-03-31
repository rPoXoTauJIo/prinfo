# --------------------------------------------------------------------------
# udp_server.py
#
# Description:
#
#   Simple udp socket server for testing
#   Listening for udp messages
#
# Credits:
#   Simple udp socket server
#   Silver Moon (m00n.silv3r@gmail.com)
#
# -------------------------------------------------------------------------
import socket
import sys
import time
import pickle
import constants as C
import config
import threading
import re
from datetime import datetime

import socket


class Network(object):
    # solution by NanoDano
    # http://www.devdungeon.com/content/unit-testing-tcp-server-client-python

    class __FakeServer(object):

        def __init__(self, listenhost, listenport):
            self.__listenhost = listenhost
            self.__listenport = listenport
            self.messages = []
            self.listen = False

        def runner(self):
            # Run a server to listen for a connection and then close it
            server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                server_sock.bind((self.__listenhost, self.__listenport))
                while 1:
                    d = server_sock.recvfrom(1024)
                    data = d[0]  # data
                    addr = d[1]  # ip and port
                    self.messages.append(data)
                    if not self.listen:
                        break
                server_sock.close()
            except socket.error:
                server_sock.close()
    
    class __FakeClient(object):
        
        def __init__(self, default_serverhost, default_serverport):
            self.__default_addr = default_serverhost
            self.__default_port = default_serverport
            self.__client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        def send_message(self, msg, addr=None, port=None):
            if addr == None:
                addr = self.__default_addr
            if port == None:
                port = self.__default_port
            try:
                self.__client.sendto(msg, (addr, port))
                return True
            except:
                return False

    def __init__(self, config):
        self.C = config
        self.server = self.__FakeServer(
            self.C['SERVERHOST'], self.C['SERVERPORT'])
        self.client = self.__FakeClient(
            self.C['CLIENTHOST'], self.C['CLIENTPORT'])

class Point(object):
    
    def __init__(self):
        pass

class Listener(object):
    
    def __init__(self):
        self.server = Network(config.C).server
        self.server.listen = True
        self.server_thread = threading.Thread(target=self.server.runner)
        self.server_thread.start()
    
    def __del__(self):
        self.server.listen = False
        self.server_thread.join()
        
class Buffer(object):
    
    def __init__(self, logger):
        self.logger = logger
        self.__buffer_size = 100
        self.__buffer = []
        threading.Thread(target=self.runner).start()
        
    def get_latest_data(self, amount):
        return None

    def runner(self):
        while 1:
            try:
                last_message = self.logger.messages.pop()
            except IndexError:
                continue

            point = Point(last_message)
            if not point.valid:
                continue
            else:
                self.__buffer.append(point)
                self.__buffer.sort(key=lambda point: point.time_wall, reverse=True)
                if len(self.__buffer)>self.__buffer_size:
                    self.__buffer.pop()

class Frame(object):
    
    def __init__(self, buffer):
        self.buffer = buffer
        self.angle = 0.0
        self.time = 0.0
        self.angle_second = 0.0
        self.calculate_turn_data()
    
    def calculate_turn_data(self):
        data = self.buffer.get_latest_data(2)
        if data is None:
            return (0.0, 0.0, 0.0)
        vector_current = data[0]
        vector_previous = data[1]
        self.angle, self.time, self.angle_second = vector_current.get_turn_data(vector_previous)

class Analyzer(object):
    
    def __init__(self):
        self.buffer = Buffer(Listener())
        print('Analyzer started')

    def run(self):
        while 1:
            turn = Frame(self.buffer)
            print('%.7s deg(%.6ss), %.7s deg\s' % (turn.angle, turn.time, turn.angle_second))
    
    
if __name__ == '__main__':
    analyzer = Analyzer()
    analyzer.run()















