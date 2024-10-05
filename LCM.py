def lcm(a,b) :
    i = 1
    while True:
        if a*i%b==0:
            return a*i
        i = i+1

l= lcm(10,25)
print(l)