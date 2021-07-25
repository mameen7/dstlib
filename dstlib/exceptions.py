import sys

class Empty:
    def __init__(self, msg):
        self._msg = msg
        print(self._msg)
        sys.exit()

class ValueError:
    def __init__(self, msg):
        self._msg = msg
        print(self._msg)
        sys.exit()