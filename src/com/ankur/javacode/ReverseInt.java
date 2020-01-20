package com.ankur.javacode;
class Solution {
    public int reverse(int x) {
        int lastDigit = 0;
        int reversed = 0;
        while(x != 0){

            lastDigit = x % 10;
            if(reversed > Integer.MAX_VALUE/10 || reversed < Integer.MIN_VALUE/10)
                return 0;
            else if((reversed == Integer.MAX_VALUE/10 && lastDigit > 7) || (reversed == Integer.MIN_VALUE/10 && lastDigit < -8))
                return 0;
            else {
                reversed = reversed * 10 + lastDigit;
                x = x / 10;
            }

        }
        return reversed;
    }

    public static void main(String[] args) {

        Solution s  = new Solution();
        System.out.println(s.reverse(123));
        System.out.println(s.reverse(-123));
        System.out.println(s.reverse(-1563847412));
        System.out.println(s.reverse(-2147483648));
    }
}