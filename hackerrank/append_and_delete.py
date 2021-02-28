def appendAndDelete(s, t, k):
    smaller_length = s if len(s) < len(t) else t
    stop_point = len(smaller_length)

    for i in range(len(smaller_length) + 1):
        if i == stop_point or s[i] != t[i]:
            remaining_length_of_s = len(s[i:])
            remaining_length_of_t = len(t[i:])
            sum_of_remaining_length = remaining_length_of_s + remaining_length_of_t
            difference = k - sum_of_remaining_length 
            print(difference)

            if difference < 0:
                return "No"
            else:
                return "Yes"

    return "Yes" 

print(appendAndDelete('abcd', 'abcdert', 10))