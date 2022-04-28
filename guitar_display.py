import guitar

a=guitar.Guitar(0)
print(a.display_scale()[1],"\n")

b=guitar.Guitar(0,'regular7','major_scale',12,7)
print(b.display_scale()[1])
"""
for i, j in b.display_scale()[1].items():
    print(i,j)
"""