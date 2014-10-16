class Solution:
    def plusOne(self, digits):
        if len(digits) == 0:
            return digits
        ptr = len(digits) - 1
        add = True
        while ptr >= 0:
            digits[ptr] += 1
            if digits[ptr] > 9:
                digits[ptr] = 0
            else:
                add = False
                break
            ptr -= 1
        if add:
            digits.insert(0, 1)
        return digits

def main():
    test = Solution()
    print test.plusOne([9,9,9,9])
    print test.plusOne([1,0,3,5])

if __name__ == "__main__":
    main()
