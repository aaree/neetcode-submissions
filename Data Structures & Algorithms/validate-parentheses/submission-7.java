class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map=new HashMap<>();
        map.put(')','(');
        map.put(']','[');
        map.put('}','{');
        Deque<Character> deque=new ArrayDeque<>();
        for (int i=0;i<s.length();i++){
            if (deque.size()==0){
                deque.push(s.charAt(i));
            }
            else{
                if (map.containsKey(s.charAt(i))){
                    if (map.get(s.charAt(i)).equals(deque.peek())){
                        deque.pop();
                    }
                    else{
                        deque.push(s.charAt(i));
                    }

                }
                else{
                    deque.push(s.charAt(i));
                }
            }
        }
        if (deque.size()==0){
            return true;
        }
        else{
            return false;
        }

    }
}
