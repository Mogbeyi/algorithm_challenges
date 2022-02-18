def solution(arr):
    chunk = len(arr) // 4
    start, end = 0, chunk
    values = []
    weather = ['WINTER', 'SPRING', 'SUMMER', 'AUTUMN']

    if len(arr) == 4:
        return weather(arr.index(max(arr)))

    for _ in range(4):
        calc = abs(sub(arr[start: end]))
        values.append(calc)
        start, end = start + chunk, end + chunk

    max_index = values.index(max(values))

    return weather[max_index]

sub = lambda arr: max(arr) - min(arr) 


print(solution([2,-3,3,1,10,8,2,5,13,-5,3,-18]))
