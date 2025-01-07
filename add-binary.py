class Solution:
    def addBinary(self, a: str, b: str) -> str:
        stack = 0
        len_a = len(a)
        len_b = len(b)
        i1 = len_a-1
        i2 = len_b-1
        res_list = []
        while i1>=0 or i2>=0:
            if i1<0:
                cur_a = 0
            else:
                cur_a = int(a[i1])

            if i2<0:
                cur_b = 0
            else:
                cur_b = int(b[i2])

            cur = cur_a + cur_b + stack
            stack = cur//2
            res_list.append(cur%2)

            i1-=1
            i2-=1

        if stack:
            res_list.append(stack)

        res_list = res_list[::-1]
        res_list = [str(x) for x in res_list]
        res_list = ''.join(res_list)
        return res_list

        
