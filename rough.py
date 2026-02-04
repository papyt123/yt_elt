def ff():
    l = list(range(20))

    #print(l)

    for i in range(0,len(l), 4):
      yield l[i:i+4]

res = list(ff())

res2 = ''.join(*res)
print(res2)
