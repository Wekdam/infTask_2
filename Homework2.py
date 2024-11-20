print ("Program rozpoczol dzialanie")
while True:
    inp = input()
    if inp == "stop":
        print("Program zkonczyl dzialanie")
        break
    elif inp == "a":
        a = float(input("a -"))
        b = float(input("b -"))
        c = float(input("c -"))
        print(f"v_prostopadloscian = {bryly.v_prostopadloscian(a,b,c)}")
    elif inp == "b":
        r = float(input("r -"))
        print(f"{bryly.v_koli(r)}")
    elif inp == "c":
        c = float(input("c -"))
        print(f"{bryly.V_szeszcian(c)}")
    elif inp == "d":
        r = float(input("r -"))
        H = float(input("H -"))
    elif inp == "e":
        pass
    elif inp == "f":
        pass
    else:
        print("niema takiej komedy")