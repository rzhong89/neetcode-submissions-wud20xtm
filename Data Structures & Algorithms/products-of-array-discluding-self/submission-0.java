class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        int prefix = 1;
        res[0] = prefix;
        for (int i = 1; i < nums.length; i++) {
            prefix *= nums[i-1];
            res[i] = prefix;
        }

        int postfix = 1;
        res[nums.length-1] *= postfix;
        for (int i = nums.length - 2; i >= 0; i--) {
            postfix *= nums[i+1];
            res[i] *= postfix;
        }
        return res;
    }
}
