import threading
import time


class Philosopher(threading.Thread):
    hungry = True

    def __init__(self, index, leftChopstick, rightChopstick, isDeadlock=False):
        threading.Thread.__init__(self)
        self.index = index
        self.leftChopstick = leftChopstick
        self.rightChopstick = rightChopstick
        self.isDeadlock = isDeadlock

    def run(self):
        while self.hungry:
            time.sleep(5)
            print('%s is hungry' % self.index)
            if self.isDeadlock:
                self.deadlock()
            else:
                self.no_deadlock()

    def deadlock(self):
        chopstick1, chopstick2 = self.rightChopstick, self.leftChopstick
        while self.hungry:
            has1 = chopstick1.acquire()
            has2 = chopstick2.acquire()
            if has1 and has2:
                break
        else:
            return
        self.eat()
        chopstick2.release()
        chopstick1.release()

    def no_deadlock(self):
        chopstick1, chopstick2 = self.rightChopstick, self.leftChopstick
        while self.hungry:
            chopstick1.acquire()
            locked = chopstick2.acquire(False)
            if locked:
                break
            chopstick1.release()
            print('%s will try other chopstick' % self.index)
            chopstick1, chopstick2 = chopstick2, chopstick1
        else:
            return
        self.eat()
        chopstick2.release()
        chopstick1.release()

    def eat(self):
        print('%s starts eating' % self.index)
        time.sleep(5)
        print('%s finishes eating and thinking' % self.index)


def main():

    chopsticks = [threading.Semaphore() for n in range(5)]

    # NO DEADLOCK SOLUTION
    philosophers = [Philosopher(i, chopsticks[i % 5], chopsticks[(i+1) % 5]) for i in range(5)]

    Philosopher.hungry = True
    for x in philosophers:
        x.start()
    time.sleep(10)
    Philosopher.hungry = False
    print('End')

    # DEADLOCK SOLUTION
    philosophers = [Philosopher(i, chopsticks[i % 5], chopsticks[(i+1) % 5], True) for i in range(5)]

    Philosopher.hungry = True
    for x in philosophers:
        x.start()
    time.sleep(10)
    Philosopher.hungry = False
    print('End')


if __name__ == '__main__':
    main()