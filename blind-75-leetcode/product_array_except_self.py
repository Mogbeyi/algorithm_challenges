def product_array_except_self(nums):
    prefix_result = calc_prefix(nums)
    suffix_result = calc_suffix(prefix_result, nums)

    return suffix_result

def calc_prefix(nums):
    result = [1] * len(nums)
    product_sum = 1

    for i in range(len(nums)):
        result[i] *= product_sum
        product_sum *= nums[i]

    return result

def calc_suffix(prefix_result, nums):
    product_sum = 1
    N = len(nums)

    for i in range(N - 1, -1, -1):
        prefix_result[i] *= product_sum
        product_sum *= nums[i]

    return prefix_result 

print(product_array_except_self([1,2,3,4]))
print(product_array_except_self([1,2,3]))
print(product_array_except_self([-1,1,0,-3,3]))


