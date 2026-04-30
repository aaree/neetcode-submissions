/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        List<Interval> list=new ArrayList<>();
        intervals.sort((a,b)->a.start-b.start);
        for (Interval interval:intervals){
            if (list.size()==0){
                list.add(interval);
            }
            else{
                if (list.get(list.size()-1).end>interval.start){
                    return false;
                }
                else{
                    list.add(interval);
                }
            }

        }
        return true;
    }
}
