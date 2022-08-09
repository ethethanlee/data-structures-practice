nums = [3,3]
target = 6
# class solution(object):
def two_sum(nums, target):
    nn = 0
    for n in range(len(nums)):
        nnn = nn +1
        first = nums.pop(0)
        for number in nums:
            if (number + first) == target:
                return [nn, nnn]
            else:
                nnn = nnn + 1
        nn = 1 + nn
        
print(two_sum(nums, target))