class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length()!=t.length()){
            return false;
        }
        Map<Character, Integer> mapS=new HashMap<>();
        Map<Character, Integer> mapT=new HashMap<>();
        for (int i=0;i<s.length();i++){
            mapS.merge(s.charAt(i),1,Integer::sum);
            mapT.merge(t.charAt(i),1,Integer::sum);

            //mapS.put(s.charAt(i), mapS.getOrDefault(s.charAt(i),0)+1);
            //mapT.put(t.charAt(i), mapT.getOrDefault(t.charAt(i),0)+1);
        }
        return mapS.equals(mapT);

    }
}
