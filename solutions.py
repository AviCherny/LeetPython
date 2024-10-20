import math
from typing import List


class FirstDay:
    def max_consecutive_one(self, array:List):
        """

        Given a binary array nums, return the maximum number of consecutive 1's in the array.

        """
        max_ones_repeat = 0
        tries_one_repeat = 0
        for num in array:
            if num == 1:
                tries_one_repeat+=1
            else:
                if tries_one_repeat > max_ones_repeat:
                    max_ones_repeat = tries_one_repeat
                tries_one_repeat = 0
        if tries_one_repeat > max_ones_repeat:
            max_ones_repeat = tries_one_repeat
        return max_ones_repeat

    def find_numbers_with_even_number_of_digits(self, nums:List):
        """
        Given an array nums of integers, return how many of them contain an even (2,4)number of digits.

        """
        amount_even_numbers = 0
        for num in nums:
            amount_of_numbers = len(str(abs(num)))
            if amount_of_numbers%2 == 0:
                amount_even_numbers+=1
        return amount_even_numbers


    def  squares_of_sorted_array(self, nums):
        """

        Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

        """

        arr = [num*num for num in nums ]
        return sorted(arr)






if __name__ == '__main__':
    my_array = nums = [-10,-5,-1,2,8 ]
    solution = FirstDay()
    print(solution.squares_of_sorted_array(my_array))
