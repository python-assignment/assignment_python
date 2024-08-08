sl = 'abcdefghijklmnopqrstuvwxyz'
cl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit = '0123456789' 
sc = '@#$%^&*!'
min_character = 6
max_character = 12
pasword = input ("enter the password :").split(',')
for i in pasword:
    i = i.strip()
    if len(i)>=6 and len(i)<=12 and (b in sl for b in i) and (c in cl for c in i) and (d in digit for d in i) and (e in sc for e in i):
        print(i)
