class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length()>s2.length()){
            return false;
        }
        if (s1.equals(s2)){
            return true;
        }
        int[] s1A=new int[26];
        int[] s2A=new int[26];
        for (char c:s1.toCharArray()){
            s1A[c-'a']++;
        }
        int l=0;
        int r=0;
        char[] s2Arr=s2.toCharArray();
        int minWindow=Integer.MAX_VALUE;
        while (r<s1.length()){
            s2A[s2Arr[r]-'a']++;
            r++;
        }
        if (Arrays.equals(s2A,s1A)){
            return true;
        }
        while (r<s2.length()){
            if (Arrays.equals(s2A,s1A)){
                return true;
            }
            s2A[s2Arr[r]-'a']++;
            s2A[s2Arr[l]-'a']--;
            r++;
            l++;
        }
        if (Arrays.equals(s2A,s1A)){
            return true;
        }        
        return false;
    }
}
