import pandas as pd
import openpyxl

class MathEnglish:
    def __init__(self, id, df):
        self.id = id
        self.df = df

    def English_enrolled(self):
        math_courses = ['Math-112', 'Math-110A', 'Math-116']
        student_df = self.df[df['Student ID'] == id]
        student_df = student_df.reset_index()
        for i in range(len(student_df)):
            if student_df.loc[i, 'Course Number'] == 'ENGL-100':
                english_course = df.loc[i, 'Course Number']

            if student_df.loc[i, 'Course Number'] == 'ENGL-100S':
                english_course = df.loc[i, 'Course Number']

            if student_df.loc[i, 'Course Number'] in math_courses:
                math_course = student_df.loc[i, 'Course Number']
        print(english_course, math_course)
        return english_course





df = pd.read_csv('C:/Users/fmixson/Desktop/Dashboard_files/LCP_English_Math/campus-v2report-enrollment-2023-05-11 (1).csv')
pd.set_option('display.max_columns', None)
df = df[df['Dropped'] == 'No'].reset_index()
id_list = []
for i in range(len(df)):
    if df.loc[i, 'Student ID'] not in id_list:
        id_list.append(df.loc[i, 'Student ID'])

for id in id_list:
    student = MathEnglish(id, df)
    student.English_enrolled()



# df[['First', 'Second', 'Third']] = df.Dropped.str.split(',', expand=True)
# print(df)

