import time
import sys

name = input("What is your name?")

if name == name:
    print("I"), time.sleep(2.0)
    print("Love"), time.sleep(2.0)
    print("You"), time.sleep(2.0)

    def delay_name(n):
        for e in n:
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.25)

    delay_name(name)
