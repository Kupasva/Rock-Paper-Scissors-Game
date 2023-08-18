import os,time



os.system('cls')
files = ["tesst.txt", "tesst2.txt"]
frames= []

for name in files:
    with open(name,"r", encoding="utf8") as f:
        frames.append(f.readline())

for frame in frames:
    print("".join(frame))
    time.sleep(1)
    os.system('cls')