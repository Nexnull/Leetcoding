one = [94,209,246,254,93,
       182,31,225,187,205,
       125,7,203,245,218,
       52,254,212,15,214,
       243,76,31,187,18]

two = [216,64,45,191,48,
       109,210,220,205,64,
       50,144,97,251,241,
       164,221,226,1,20,
       169,87,113,121,31]

a,b,c,d = 0,0,0,0
for i in one:
    if 0<=i and i <=63:
        a += 1
    if 64<=i and i<=127:
        b += 1
    if 128<=i and i<=191:
        c += 1
    if 192<=i and i<=255:
        d += 1

print(a,b,c,d,a+b+c+d)

a,b,c,d = 0,0,0,0
for i in two:
    if 0<=i and i <=63:
        a += 1
    if 64<=i and i<=127:
        b += 1
    if 128<=i and i<=191:
        c += 1
    if 192<=i and i<=255:
        d += 1
print(a,b,c,d,a+b+c+d)


"""
Histogram Equalization is a computer image processing technique used to improve contrast in images .
flattening the pixel in histogram evenly and changing amount of pixels 
Using grayscala mapping function to do this process to make sure do not loss any pixels


To convert a frequency distribution to a probability distribution and
divide area of the bar or interval of x by the total area of all the Bars.
"""