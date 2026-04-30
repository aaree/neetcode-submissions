class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans=new int[nums.length];
        int[] reversed= new int[nums.length];
        List<Integer> forward=new ArrayList<>();
        List<Integer> back=new ArrayList<>();
        int product=1;
        int reverse=1;
        for(int i=0;i<nums.length;i++){
            reversed[nums.length-i-1]=nums[i];
        }
        for (int num:nums){

            forward.add(product);
            product*=num;
        }
        for (int rev: reversed){
            back.add(reverse);
            reverse*=rev;            
        }
        for (int j=0;j<ans.length;j++){
            ans[j]=forward.get(j)*back.get(back.size()-j-1);
        }
        return ans;


    }
}  
