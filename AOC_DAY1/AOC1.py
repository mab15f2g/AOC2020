report = []

with open ("report") as file:
    report = list(map(int, file.read().splitlines() ))    



for a in report:
    for b in report:
        for c in report:
            if  a + b + c == 2020:
                print (a*b*c)
    