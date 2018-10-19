class Request(object):
    _lifetime = 0
    _processing_time = 0

    def __init__(self, lifetime=2, processing_time=4):
        self._lifetime = lifetime
        self._processing_time = processing_time

    def get_processing_time(self):
        return self._processing_time

    def is_dead(self):
        if self._lifetime <= 0:
            return True
        return False

    def live_day_again(self):
        if self._lifetime > 0:
            self._lifetime = self._lifetime - 1

