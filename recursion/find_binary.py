def find_binary(decimal):
    result = []

    def solution(decimal):
        if decimal == 0:
            return 

        result.append(str(decimal % 2)) 

        return solution(decimal // 2)

    solution(decimal)

    return ''.join(result[::-1]) 
