class Solution {
    public boolean isHappy(int n) {
        
        HashSet<Integer> seen = new HashSet<Integer>();
        
        int fun = n;
        while(!seen.contains(fun)) {
            seen.add(fun);
            int sum = 0;
            while (fun > 0) {
                int dub = fun % 10;
                fun = fun / 10;
                sum += dub * dub;
            }
            if (sum == 1) {
                return true;
            }
            fun = sum;
        }
        return false;
    }
}
