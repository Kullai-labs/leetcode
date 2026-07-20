class Solution(object):
    def shiftGrid(self, grid, k):
        m,n =len(grid),len(grid[0])
        flat=[x for row in grid for x in row]
        k%=(m*n)
        flat=flat[-k:]+flat[:-k]
        return [flat[i*n :(i+1)*n] for i in range(m)]


        