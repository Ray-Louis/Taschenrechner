print("created by RLN")
print("""welchen rechner willst du haben?
1. addition
2. subtraktion
3. Division
4. multiplikation""")
bed = int(input("==> "))
value1 = input("Erste Zahl eingeben:  ")
value2 = input("Zweite Zahl eingeben:  ")

if bed==1:
    print(float(value1) + float(value2))
if bed==2:
    print(float(value1) - float(value2))
if bed==3:
    print(float(value1) / float(value2))
if bed==4:
    print(float(value1) * float(value2))
print("created by RLN")
input(exit)


