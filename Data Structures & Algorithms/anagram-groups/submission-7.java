class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>>map=new HashMap<>();
        for (String str:strs){
            char[] temp=str.toCharArray();
            int[] temp2=new int[26];
            for (char c:temp){
                temp2[c-'a']++;
                //System.out.println(temp);
            }
            String key=Arrays.toString(temp2);
            if (!map.containsKey(key)){
                map.put(key,new ArrayList<>());
            }
            map.get(key).add(str);

        }
        List<List<String>>list=new ArrayList<>();
        for (Map.Entry<String,List<String>> e : map.entrySet()){
            list.add(e.getValue());

        }
        return list;
    }
}
