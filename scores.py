student_list={
    'Job':{'数学':89,'英语':92},
    'Mary':{'数学':93,'英语':98},
    'Ben':{'数学':99,'英语':88},
}
def query_student():
    name=input("学生姓名：").strip()
    if name in student_list:
        scores=student_list[name]
        print(f"\n{name}的成绩：")
    for subject,score in scores.items():
        print(f"\n{subject}:{score}分")
query_student()