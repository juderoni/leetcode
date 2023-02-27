class Solution {
    public int titleToNumber(String columnTitle) {
        int power = columnTitle.length() - 1;
        int sum = 0;
        for (int i = 0; i < columnTitle.length(); i++) {
            int base = 1;
            if (power > 0) {
                base = (int) Math.pow(26,power);
            }
            sum += base * findValForChar(columnTitle.charAt(i));
            power--;
        }
        return sum;
    }

    private int findValForChar(char ting) {
        // int track = 1;
        char s = 'A';
        for (int i = 1; i <= 26; i++) {
            if (ting == s) {
                return i;
            }
            else {
                s = (char)(s + 1);
            }
        }
        return -1;
    }
    
}
