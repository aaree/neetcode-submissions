class Solution {
    public boolean isPalindrome(String s) {
        int l=0;
        int r=s.length()-1;
        while (r>l){
            if (!Character.isLetterOrDigit(Character.toLowerCase(s.charAt(r)))){
                r--;
            }
            else if (!Character.isLetterOrDigit(Character.toLowerCase(s.charAt(l)))){
                l++;
            }
            else{
                if (Character.toLowerCase(s.charAt(r))!=Character.toLowerCase(s.charAt(l))){
                    return false;
                }
                l++;
                r--;
            }

        }
        return true;
    }
}
