s = input()
if "SS" in s:
    a, b = s.split("SS")
    a = a.lower()
    b = b.lower()
    count = 2
    if b != "":
        if b[0] == "s":
            count = 3
            b = b[1:]

    print(a + count*"s" + b)
    if count == 2:
        print(a + "B" + b)
    else:
        print(a + "Bs" + b)
        print(a + "sB" + b)
else: print(s.lower())