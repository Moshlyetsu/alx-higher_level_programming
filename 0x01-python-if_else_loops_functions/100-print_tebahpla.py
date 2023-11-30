#!/usr/bin/python3
alphbt = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - alphbt)), end="")
    alphbt = 32 if alphbt == 0 else 0
