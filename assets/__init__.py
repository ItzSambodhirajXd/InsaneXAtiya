import os

boobs = []

for pussy in os.listdir("assets"):
    if pussy.endswith("png"):
        boobs.append(pussy[:-4])
