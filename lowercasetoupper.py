name="harsh"
result=""

for ch in name:
    if ch>="a" and ch<="z":
        result+=chr(ord(ch)-32)

print(f"the upper case is : {result}")