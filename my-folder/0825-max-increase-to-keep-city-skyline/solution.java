class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int orgSum = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                int minmax = minMaxTing(grid, i, j);
                orgSum+=grid[i][j];
                grid[i][j] = minmax;
            }
        }

        int sum = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                sum+=grid[i][j];
            }
        }
        return sum - orgSum;
        
    }

    private int minMaxTing(int[][] grid, int row, int col) {
        int maxRow = grid[row][col];
        int maxCol = grid[row][col];
        for (int i = 0; i < grid.length; i++) {
            if (grid[row][i] > maxRow ) {
                maxRow = grid[row][i];
            }
            if (grid[i][col] > maxCol ) {
                maxCol = grid[i][col];
            }
        }
        //returns min
        if (maxCol > maxRow) {
            return maxRow;
        }
        else {
            return maxCol;
        }
    }
}
