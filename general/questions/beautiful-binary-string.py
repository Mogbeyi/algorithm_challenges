def beautifulBinaryString(b):
    minimum_moves = 0
    
    while (len(b) >= 3):
        if '010' in b:
            minimum_moves += 1
        if len(b) <= 3:
            break
        elif b[3] == '0':
            b = b[3:]
        elif b[3] == '1':
            b = b[4:]
    
    return minimum_moves


print(beautifulBinaryString('0100101010100010110100100110110100011100111110101001011001110111110000101011011111011001111100011101'))
print(beautifulBinaryString('100110110011111101110100011011101000011010111001001011010010110010111011100000000100011111100101010'))


