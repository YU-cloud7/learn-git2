class Student:
    def __init__(self,name,age,scores): 
        self.name=name
        self.age=age
        self.scores=scores
    def calculate_average(self):
        if len(self.scores)==0:
            return 0.0
        return sum(self.scores)/len(self.scores)
    def display_scores(self):
        scores0=self.calculate_average()
        print(f"姓名:{self.name}.年龄:{self.age},平均成绩:{scores0:.2f}")
    
student1=Student("Any",18,[85,90,78])
student2=Student("Bob",19,[92,88,76])


student3=Student("Mike",20,[80,85,90])
student1.display_scores()
student2.display_scores()
student3.display_scores()