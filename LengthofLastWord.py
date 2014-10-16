class Solution:
    def lengthOfLastWord(self, s):
        if s == "":
            return 0
        arr = s.split(' ')
        ptr = len(arr) - 1
        while ptr >= 0:
            if arr[ptr] != '':
                return len(arr[ptr])
            ptr -= 1
        return 0

def main():
    test = Solution()
    print test.lengthOfLastWord("hello world ")

if __name__ == "__main__":
    main()
