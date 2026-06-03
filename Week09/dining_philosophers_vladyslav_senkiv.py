import threading
import time
import random


class Fork:
    def __init__(self, number):
        self.number = number
        self.lock = threading.Lock()


class Philosopher(threading.Thread):
    def __init__(self, number, left_fork, right_fork, meals_count=3):
        super().__init__()
        self.number = number
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.meals_count = meals_count

    def think(self):
        print(f"Philosopher {self.number} is thinking")
        time.sleep(random.uniform(0.5, 1.5))

    def eat(self):
        print(f"Philosopher {self.number} is eating")
        time.sleep(random.uniform(0.5, 1.5))

    def run(self):
        for _ in range(self.meals_count):
            self.think()

            if self.number % 2 == 0:
                first_fork = self.left_fork
                second_fork = self.right_fork
            else:
                first_fork = self.right_fork
                second_fork = self.left_fork

            with first_fork.lock:
                print(f"Philosopher {self.number} took fork {first_fork.number}")

                with second_fork.lock:
                    print(f"Philosopher {self.number} took fork {second_fork.number}")
                    self.eat()

                print(f"Philosopher {self.number} released fork {second_fork.number}")

            print(f"Philosopher {self.number} released fork {first_fork.number}")


if __name__ == "__main__":
    philosophers_count = 5
    forks = [Fork(i) for i in range(philosophers_count)]

    philosophers = []

    for i in range(philosophers_count):
        philosopher = Philosopher(
            number=i,
            left_fork=forks[i],
            right_fork=forks[(i + 1) % philosophers_count],
            meals_count=3
        )
        philosophers.append(philosopher)

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()

    print("Dinner is finished")
