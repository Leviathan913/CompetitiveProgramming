class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans = [[0]*n for _ in range(m)]
        
        for i in range(len(img)):
            for j in range(len(img[i])):
                s = img[i][j]
                count = 1
                if i - 1 >= 0:
                    s += img[i-1][j]
                    count += 1
                if i + 1 < m:
                    s += img[i+1][j]
                    count += 1
                if j - 1 >= 0:
                    s += img[i][j-1]
                    count += 1
                if j + 1 < n:
                    s += img[i][j+1]
                    count += 1
                if i - 1 >= 0 and j - 1 >= 0:
                    s += img[i-1][j-1]
                    count += 1
                if i - 1 >= 0 and j + 1 < n:
                    s += img[i-1][j+1]
                    count += 1
                if i + 1 < m and j - 1 >= 0:
                    s += img[i+1][j-1]
                    count += 1
                if i + 1 < m and j + 1 < n:
                    s += img[i+1][j+1]
                    count += 1

                ans[i][j] = s//count

        return ans