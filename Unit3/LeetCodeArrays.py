# 1. Two Sum

    #give an array of integers nums and an 
    #integer target, return the indices of the two numbers 
    # such that they add up to target

    #example: 
        #Input: nums = [2, 7, 11, 15], target = 9
        #Output: [0, 1]
        #Explanation: nums[0] + nums[1] = 2 + 7 = 9

def two_sum(nums, target):
    hashmap = []
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = 1


# 2. Best time to buy and sell stock
    
    #You are given an array prices where prices[i] is 
    #the price of a given stock on the i-th day. You 
    #want to maximize your profit by choosing a single 
    #day to buy one stock and choosing a different day in 
    #the future to sell that stock.

    #example:
        #Input: prices = [7, 1, 5, 3, 6, 4]
        # Output: 5
        # Explanation: Buy on day 2 (price = 1) and sell on 
        # day 5 (price = 6), profit = 6 - 1 = 5.

    def max_profit(prices):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
              min_price = price
            elif price - min_price > max_profit:
             max_profit = price - min_price
        return max_profit

# 3. Product of Array Except Self
    #Problem Statement: Given an integer array nums, 
    #return an array answer such that answer[i] is equal 
    #to the product of all the elements of nums except nums[i].

    #Example:
        #Input: nums = [1, 2, 3, 4]
        # Output: [24, 12, 8, 6]
        # Explanation:
        #    For index 0: product of [2, 3, 4] is 24.
        #    For index 1: product of [1, 3, 4] is 12. And so on.

    def product_except_self(nums):
        length = len(nums)
        answer = [1] * length

        # Calculate left products.
        left = 1
        for i in range(length):
            answer[i] = left
            left *= nums[i]

        # Calculate right products and combine with left products.
        right = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer

