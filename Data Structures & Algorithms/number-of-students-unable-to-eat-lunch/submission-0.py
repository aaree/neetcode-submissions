class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student=deque(students)
        sand=deque(sandwiches)
        while student:
            if sum(student)==0:
                if sand[0]==1:
                    break
            if sum(student)==len(student):
                if sand[0]==0:
                    break
            if student[0]==sand[0]:
                student.popleft()
                sand.popleft()
            else:
                new=student.popleft()
                student.append(new)
        return len(student)