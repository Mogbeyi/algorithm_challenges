def merge_meetings(arr):
    '''
    if end time of first meeting >= start time of next meeting, merge time meetings
    Example:[(1, 3), (2, 4)] -> [(1, 4)]
    Example:[(1, 3), (3, 5)] -> [(1, 5)]
    '''

    sorted_arr = sorted(arr)
    

