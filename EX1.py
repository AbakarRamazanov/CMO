import time
import random
import Const
from threading import Thread


class Requester(Thread):
    def __init__(self, range_amount_create=(1, 3), range_time_create=(1, 3), time_processing_requests=4):
        Thread.__init__(self)
        self.range_amount_create = self._check_amount_or_time(range_amount_create)
        self.range_time_create = self._check_amount_or_time(range_time_create)
        self.requests = list()
        self.time_processing_requests = time_processing_requests
        random.seed()
        pass

    def run(self):
        while True:
            if Const.DEBUG:
                print("\n\n*********DEBUG*********\n\t***Requester***")
                print("amount_living_requests \t= " + str(self.amount_living_requests))
                print("amount_dead_requests \t= " + str(self.amount_dead_requests))
                print("_amount_get_request \t= " + str(self._amount_get_request))
                print("_delay_new_requests \t= " + str(self._delay_new_requests))
                print("len(self.requests) \t\t= " + str(len(self.requests)))
                pass
            if self._amount_get_request != 0:
                self.requests = self.requests[
                                self._amount_get_request:]  # удаляем из списка запрошенные элементы
                _amount_get_request = 0
                pass
            if not self._delay_new_requests:
                self._add_new_requests()
                pass
            else:
                self._step()
                pass
            time.sleep(0.5)
            pass

    def get_part(self, amount):
        pass

    def how_much_is_thrown_away(self):
        return self.amount_thrown_away

    requests = 0  # список запросов
    amount_living_requests = 0  # количество живых запросов
    amount_dead_requests = 0  # количество мертвых запросов
    range_amount_create = (0, 0)  # диапазон количества для создания
    range_time_create = (0, 0)  # диапазон времени для создания
    time_processing_requests = 0
    _amount_get_request = 0  # количество полученных запросов для удаления
    _delay_new_requests = 0

    def _check_amount_or_time(self, _tuple):
        # TODO проверка на отрицательные значения
        if _tuple[0] > _tuple[1]:
            _tuple = tuple(_tuple[1], _tuple[0])
        elif _tuple[0] > _tuple[1]:
            _tuple = tuple(_tuple[1], _tuple[0] + 1)
        return _tuple
        pass

    def _add_new_requests(self):
        count_new_requests = self._get_count_new_requests()
        for n in range(count_new_requests):
            self.requests.append(Request())
            pass
        self._delay_new_requests = random.randint(self.range_time_create[0], self.range_time_create[1])
        pass

    def _get_count_new_requests(self):
        return random.randint(self.range_amount_create[0], self.range_amount_create[1])
        pass

    # def _get_delay_new_requests(self):
    #     return random.randint(self.range_time_create[0], self.range_time_create[1])
    #     pass

    def _step(self):
        self._delay_new_requests = self._delay_new_requests - 1
        [request.live_day_again() for request in self.requests]
        self._funeral()

    def _funeral(self):
        count = 0
        count_requests = len(self.requests)
        while count < count_requests:
            if self.requests[count].is_dead():
                self.amount_dead_requests = self.amount_dead_requests + 1
                self.requests.pop(count)
                count_requests = len(self.requests)
            else:
                count = count + 1
                pass


class Request(object):
    _lifetime = 0
    _processing_time = 0

    def __init__(self, lifetime=2, processing_time=4):
        self._lifetime = lifetime
        self._processing_time = processing_time

    def get_processint_time(self):
        return self._processing_time

    def is_dead(self):
        if self._lifetime <= 0:
            return True
        return False

    def live_day_again(self):
        if self._lifetime > 0:
            self._lifetime = self._lifetime - 1


if __name__ == '__main__':
    requester = Requester()
    requester.start()
    while True:
        print("I'm other thread!")
        print("I'm other thread!")
        print("I'm other thread!")
        print("I'm other thread!")
        print("I'm other thread!")
        print("I'm other thread!")
        print("I'm other thread!")
        print("I'm other thread!")
        time.sleep(2)
        pass
