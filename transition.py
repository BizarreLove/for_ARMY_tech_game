import base64

n_table = "1234567890"
a_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
cipher = "gra0jL8qh08vTEDpWJS0TNP1W9rWYJTYOYKn"

for r1 in range(100):
    for r2 in range(100):

        plain = ""

        for i in range(len(cipher)):
            if a_table.find(cipher[i]) >=0:
                position = ( a_table.find(cipher[i]) + r1 ) % 52                              
                plain = plain + a_table[position]

            elif n_table.find(cipher[i]) >=0:
                position = ( n_table.find(cipher[i]) + r1 + r2 ) % 10
                plain = plain + n_table[position]

            else:
                plain = plain + cipher[i]
        
        plain = base64.b64decode(plain)
        
        try:
            plain = plain.decode("ascii")
            print(plain)
        except:
           continue


