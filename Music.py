st = "--------------------------"
st2 = "--------------------------"
j = 597
k = 0
di = {
    "-" : "zz",
    "c" : "do",
    "d" : "re",
    "e" : "mi",
    "f" : "fa",
    "g" : "sol",
    "a" : "la",
    "b" : "si"
}
st3 = ""
for i in st:
    i = i.lower()
    m = st2[k].lower()
    if m != '-' and i == '-':
        i = m
    st3 += i
    s = f"when {j} =>\nif count < step then\ncount <= count + 1; frecuencyController <= {di[i]};\nelse\nsteper <= steper + 1; count <= 0;\nend if;"
    print(s)
    j += 1
    k += 1