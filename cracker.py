import hashlib
import os

def md5sum(word):
    md5 = hashlib.md5()
    md5.update(word.encode())
    hex_dig = md5.hexdigest()
    return hex_dig

def sha256sum(word):
    sha256 = hashlib.sha256()
    sha256.update(word.encode())
    hex_dig = sha256.hexdigest()
    return hex_dig

def black2bsum(word):
    black2b = hashlib.blake2b()
    black2b.update(word.encode())
    hex_dig = black2b.hexdigest()
    return hex_dig

def black2ssum(word):
    black2s = hashlib.blake2s()
    black2s.update(word.encode())
    hex_dig = black2s.hexdigest()
    return hex_dig





filePath = input("Path of your file: ")
tries = 0

#c378985d629e99a4e86213db0cd5e70d

method = input("which encryption algorithm do you want to crack: " )
print("")
algorithms = ["md5", "sha256","black2b","black2s"]
for algorithm in algorithms:
    print(algorithm.upper(), end=" ")
print("")
sum = input("Enter the hash you want to crack: ")



if method == "md5":
    with open(filePath, "r") as file:
        for line in file:
            os.system("cls")
            tries += 1
            if md5sum(line.strip()) == sum:
                print(tries, "tries")
                print("Continued your hash is equals to ",line)
                break
            else:
                print(tries,"tries")
                continue
            


elif method == "sha256":
    with open(filePath, "r") as file:
        for line in file:
            os.system("cls")
            tries += 1
            if sha256sum(line.strip()) == sum:
                print(tries, "tries")
                print("Continued your hash is equals to ",line)
                break
            else:
                print(tries,"tries")
                continue


elif method == "black2b":
    with open(filePath, "r") as file:
        for line in file:
            os.system("cls")
            tries += 1
            if black2bsum(line.strip()) == sum:
                print(tries, "tries")
                print("Continued your hash is equals to ",line)
                break
            else:
                print(tries,"tries")
                continue


elif method == "black2s":
    with open(filePath, "r") as file:
        for line in file:
            os.system("cls")
            tries += 1
            if black2ssum(line.strip()) == sum:
                print(tries, "tries")
                print("Continued your hash is equals to ",line)
                break
            else:
                print(tries,"tries")
                continue    

else:
    print("Wrong input")
    print("Please try again...")

