import sys

def generate_serial(seed, key):
    serial = ''

    for i in range(20):
        if 97<=ord(seed[i]) and ord(seed[i])<=122:
            key1 = 26 - key % 26
            a = ord(seed[i]) + key1
            if a > 122:
                a = a - 26
            serial = serial + chr(a)


        elif 65<=ord(seed[i]) and ord(seed[i])<=90:
            key1 = 26 - key % 26
            a = ord(seed[i]) + key1
            if a > 90:
                a = a - 26
            serial = serial +chr(a)

        elif 48<=ord(seed[i]) and ord(seed[i])<=57:
            key1 =10 -  key % 10
            a = ord(seed[i]) + key1
            if a > 57:
                a = a - 10
            serial = serial + chr(a)

        if i == 3 or i == 7 or i == 11 or i == 15:
            serial = serial+'-'

    return serial

if len(sys.argv) < 3:
    print("Seed and Key not provided!!!")
    exit(1)

seed = sys.argv[1]
if len(seed) != 20:
    print("Incorrect seed format")
    exit(1)

key = int(sys.argv[2])
if key < 17 or key > 255:
    print("Incorrect key format")
    exit(1)


serial = generate_serial(seed, key)

print(serial)