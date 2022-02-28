print("Project - Crypto")
import timeit
def ember():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]
    #print(keys)
    #print(values)

    dict_e = dict(zip(keys, values))
    dict_d = dict(zip(values, keys))

    msg = input("Enter your secret message quietly: ")
    mode = input("Crypto Mode: Encode (e) OR Decode (d): ")

    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    elif mode.lower() == 'd':
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
    else:
        new_msg = "Enter e for Encode or d for Decode! Bad Value!"
    return new_msg.upper() 

print(ember())
#print(timeit.timeit('ember()', globals=globals(), number=5))
