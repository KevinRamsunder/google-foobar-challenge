def answer(digest):
    code = [0 for i in range(len(digest))]

    for i in range(len(digest)):
        for j in range(256):
            cipher = (digest[i] ^ code[i - 1]) + j * 256 
            if cipher % 129 == 0:
                code[i] = cipher / 129
                break

    return code