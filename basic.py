t = str ( input('Enter the no of terms'))
count = 0
if t == t[::-1]:
    print("its palindrome")
else:
    print("it's not a palindrome")
i = 0
j = len(t)-1
for i in range( len(t)):
    print(t[i])
    if t[i::] == t[j::-1]:
        print (" its palindrome")
    else:
        temp = j
        for k in range(temp,i,-1):
            print('temp ',t[k],str(k))
            if t[i] == t[k]:
                if t[i:k+1:] == t[k:i-1:-1]:
                    print("palindrome")
                    print(t[i:k+1:])
                    break

##if t <= 100 and t >= 1:
#    s = str( input('Enter the string '))
#    if len(s) <= 1000 and len(s) >= 1:
#        sus = s
#        res = s[::-1]
#        s.in

