import sys;rl=sys.stdin.readline

decryption = {
    '@': 'a', 
    '[': 'c', 
    '!': 'i', 
    ';': 'j', 
    '^': 'n', 
    '0': 'o', 
    '7': 't', 
    "\\'": 'v', 
    "\\\\'": 'w'
}

N = int(rl())

for _ in range(N):
    crypto = rl().strip()
    cnt_crypto = 0
    
    i = 0
    res = ''
    while i < len(crypto):
        if crypto[i:i+3] == "\\\\'":
            new_char = decryption["\\\\'"]
            cnt_crypto += 1
            i += 3
        elif crypto[i:i+2] == "\\'":
            new_char = decryption["\\'"]
            cnt_crypto += 1
            i += 2
        elif crypto[i] in decryption:
            new_char = decryption[crypto[i]]
            cnt_crypto += 1
            i += 1
        else:
            new_char = crypto[i]
            i += 1
        res += new_char
    
    print("I don't understand" if cnt_crypto >= len(res) / 2 else res)