import threading
import time
import random

pizza_sem = threading.Semaphore(value=0)
spagy_sem = threading.Semaphore(value=0)
costco_sem = threading.Semaphore(value=0)


def bake_pizza():
    time.sleep(random.randint(1, 5))
    print('releasing pizza')
    pizza_sem.release()


def cook_spaghetti():
    time.sleep(random.randint(1, 5))
    print('releasing spagy')
    spagy_sem.release()


def buy_chicken_bake():
    time.sleep(random.randint(1, 5))
    print('releasing costco')
    costco_sem.release()


def main():
    semaphore_dict = {
        'pizza_sem': False,
        'spagy_sem': False,
        'costco_sem': False
    }
    while 1:
        if not pizza_sem.acquire(blocking=False):
            print('waiting for pizza_sem...')
        else:
            semaphore_dict['pizza_sem'] = True
            print('we got pizza_sem!!!!')
        if not spagy_sem.acquire(blocking=False):
            print('waiting for spagy_sem...')
        else:
            print('we got spagy_sem!!!!')
            semaphore_dict['spagy_sem'] = True
        if not costco_sem.acquire(blocking=False):
            print('waiting for costco_sem...')
        else:
            print('we got costco_sem!!!!')
            semaphore_dict['costco_sem'] = True
        if all(value for value in semaphore_dict.values()):
            print('its been fun.', semaphore_dict.values())
            exit(0)
        time.sleep(0.2)


t1 = threading.Thread(target=bake_pizza)
t2 = threading.Thread(target=cook_spaghetti)
t3 = threading.Thread(target=buy_chicken_bake)
t4 = threading.Thread(target=main)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
