class Solution:
    def beautyNum(self, L, R, t):
        count = 0
        xor_table = [[i ^ j for i in range(16)] for j in range(16)]
        for i in range(L, R+1):
            num = str(i)
            bn = 0
            for j in num:
                bn = xor_table[bn][int(j)]
            if bn == t:
                count += 1
        print(count, end=" ")

    def forceBN(self, L, R, t):
        count = 0
        for i in range(L, R + 1):
            num = str(i)
            bn = 0
            for j in num:
                bn ^= int(j)
            if bn == t:
                count += 1
        print(count, end=" ")

    # def __init__(self):
    #     T = int(input())
    #     LQuery = input("")
    #     L = [int(n) for n in LQuery.split()]
    #     RQuery = input("")
    #     R = [int(n) for n in RQuery.split()]
    #     tQuery = input("")
    #     t = [int(n) for n in tQuery.split()]
    #     for i in range(T):
    #         self.beautyNum(L[i], R[i], t[i])

s = Solution()

s.beautyNum(10, 10000, 12)
s.forceBN(10, 10000, 12)

int Decrypt(int encryptedNumber, int decryption, int number) {
    if (decryption == 0) return 1 % number;
    int temp = Decrypt(encryptedNumber, decryption >> 1, number);
    temp = temp * temp % number;
    if (decryption & 1) temp = (int) temp * a % n;
    return temp;
}