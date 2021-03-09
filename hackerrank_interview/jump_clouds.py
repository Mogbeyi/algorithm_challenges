# def jumpingOnClouds(c):
#     if len(c) == 1:
#         return 0
#     if len(c) == 2:
#         return 0 if c[1] == 1 else 1
#     if c[2] == 1:
#         return 1 + jumpingOnClouds(c[1:])
#     if c[2] == 0:
#         return 1 + jumpingOnClouds(c[2:])

def jumpingOnClouds(c):
    minimum_jump = 0
    start = 0
    window_max = 3
    stop = len(c) 
    
    while window_max <= stop:
        sub_cloud = c[start: window_max]
        
        if sub_cloud[0] == 0 and sub_cloud[2] == 0:
            minimum_jump += 1
            start += 2
            window_max += 2
        elif sub_cloud[0] == 0 and sub_cloud[1] == 0:
            minimum_jump += 1
            start += 1
            window_max += 1
        elif sub_cloud[1] == 0 and sub_cloud[2] == 0:
            minimum_jump += 1
            start += 2
            window_max += 1
        else:
            start += 1
            window_max += 1
            
    return minimum_jump

print(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))

