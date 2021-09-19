import os, sys, time

def infinity():
    while True:
        yield

for i in infinity():
        print("hidup ...")
        os.system("xset led 3")
        time.sleep(0.3)
        os.system("xset led off")
        print("mati ...")
        time.sleep(0.3)
