def birthdayCakeCandles(candles):
    # Write your code here
    max_height_candle = max(candles)
    count = 0
    
    for num in candles:
        if num == max_height_candle:
            count += 1
    return count

