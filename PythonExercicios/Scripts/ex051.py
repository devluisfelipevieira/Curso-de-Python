n = int(input('Qual a o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))
for c in range(n,n+(10*r),r):
    print(c, end = '→ ')
print('Acabou')