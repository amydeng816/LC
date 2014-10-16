class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num) < 3:
            return 0
        num.sort()
        number = num[0] + num[1] + num[2]
        diff = abs(number - target)
        for i in range(len(num) - 2):
            left = i + 1
            right = len(num) - 1
            while left < right:
                temp = num[left] + num[right] + num[i]
                if abs(temp - target) < diff:
                    number = temp
                    diff = abs(temp - target)
                if temp == target:
                    return number
                if temp > target:
                    right -= 1
                else:
                    left += 1
        return number