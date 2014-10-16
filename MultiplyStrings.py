class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        n1 = list(num1[::-1])
        num2 = num2[::-1]
        sz1 = len(num1)
        sz2 = len(num2)
        n2 = []
        summ = []
        i = 0
        while i < sz1:
            n1[i] = int(n1[i])
            i += 1
        i = 0
        while i < sz2:
            for zero in range(i):
                n2.append(0)
            x = int(num2[i])
            q = 0
            i1 = 0
            while i1 < sz1:
                mul = q + n1[i1] * x
                q = mul / 10
                n2.append(mul % 10)
                i1 += 1
            if q != 0:
                n2.append(q)
            j = 0
            q = 0
            while j < len(n2):
                if j < len(summ):
                    s = summ[j] + q + n2[j]
                    q = s / 10
                    summ[j] = s % 10
                else:
                    s = q + n2[j]
                    q = s / 10
                    summ.append(s % 10)
                j += 1
            if q != 0:
                summ.append(q)
            i += 1
            n2 = []
        return ''.join(str(xx) for xx in summ)[::-1]