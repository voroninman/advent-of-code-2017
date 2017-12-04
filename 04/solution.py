def is_valid_passphrase(text: str) -> bool:
    words = text.strip().split(' ')
    seen = {}
    for word in words:
        word = ''.join(sorted(word))
        if word in seen:
            return False
        seen[word] = True
    return True


with open('input') as f:
    print(sum(map(is_valid_passphrase, f.readlines())))
