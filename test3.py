import sys
rl = sys.stdin.readline

# 철자 매핑 설정
mapping = {
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

# 테스트 케이스 수 입력
n = int(rl())

# 각 테스트 케이스 처리
for _ in range(n):
    crypto = rl().strip()
    cnt_crypto = 0
    
    # 첫 번째 문자 변환
    i = 0
    while i < len(crypto):
        if crypto[i:i+2] == "\\'":
            new_char = mapping["\\'"]
            cnt_crypto += 1
            i += 2
        elif crypto[i:i+3] == "\\\\'":
            new_char = mapping["\\\\'"]
            cnt_crypto += 1
            i += 3
        elif crypto[i] in mapping:
            new_char = mapping[crypto[i]]
            cnt_crypto += 1
            i += 1
        else:
            new_char = crypto[i]
            i += 1
        crypto = crypto[:i-1] + new_char + crypto[i:]
    
    # 결과 출력
    if cnt_crypto >= len(crypto) / 2:
        print("I don't understand")
    else:
        print(crypto)
