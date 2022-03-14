import time
import sys

love = "I Love You \n"
name = input("What is your name? ")

if name == name:

    def delay_name(n):
        for e in n:
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.25)

    delay_name(love)
    delay_name(name)
