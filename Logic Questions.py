# to check whether the give string as a repeated letters if so print the first repeated letter
def rep_string_check (name):
    d = {}
    for x in name:
        if x not in d.keys():
           # print (d.items())
           # print(x)
            d[x] = 1
        else:
            return x
    return "no"

print(rep_string_check("baba"))


