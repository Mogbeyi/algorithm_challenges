def beautifulBinaryString(b):
    array_of_string = list(b)
    count = 0
    
    for i in range(len(b) - 2):
        substring = array_of_string[i: i + 3]
        if ''.join(substring) == '010':
            array_of_string[i + 2] = '1'
            count += 1
            
    return count
            
def main():
	print(beautifulBinaryString('0101010'))
	print(beautifulBinaryString('010'))
	print(beautifulBinaryString('0100101010'))
	print(beautifulBinaryString('01100'))

main()

