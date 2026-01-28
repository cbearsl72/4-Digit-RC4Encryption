print("This code is to take a 4 digit number and convert it to RC4 ciphertext. This is based on Lab2 of CS106: Intro To Cybersecurity")
def rc4KeyScheduling(S,key):
    #Step 1: Key Scheduling
    j = 0
    for i in range(8):
        #swap i and j in s by using this formula: j = (j+s[i]+key[i mod 4])mod 8
        j = (j + S[i] + int(key[i % 4])) % 8
        S[i],S[j] = S[j],S[i]

    print(f"Final State of S after Key Scheduling: {S}")
    return S
def rc4Encrypting(key, message):
    n = 8
    S = list(range(n))
    S = rc4KeyScheduling(S,key)

    #Step 2: Encrypting Message
    i = 0
    j = 0
    ciphertext = []

    for digit in message:
        i = (i+1)%8
        j = (j + S[i])%8

        #Another Swap
        S[i],S[j] = S[j],S[i]

        #Index of Encrypted digit
        t = (S[i]+S[j])%8

        key_bit = S[t]

        #Encrypting Digit of Message with key_bit (XOR)
        cipherDigit = int(digit) ^ int(key_bit)
        ciphertext.append(cipherDigit)

    return ciphertext


user_key = input("Please enter a four digit number for your key: ")
plaintext = input("Please enter a four digit number representing your message: ")
cipherText = rc4Encrypting(user_key,plaintext)
print(f"Encrypted Message: {cipherText}")