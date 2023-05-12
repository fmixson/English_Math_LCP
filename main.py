import pandas as pd
import openpyxl

class MathEnglish:
    def __init__(self, id, df):
        self.id = id
        self.df = df

    def English_enrolled(self):
        english_course = None
        math_course = None
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

        if english_course == None:
            english_course = 'None'
        if math_course == None:
            math_course = 'None'
        return english_course, math_course, self.id

    def lcp(self):
        head_count_df = self.df.drop_duplicates(subset='Student ID').reset_index
        ed_plans = ['ASEP: Abbreviated Educational Plan', 'CSEP: Comprehensive Educational Plan']
        lcps = ['Arts, Humanities, & Communication', 'Applied Technology & Skilled Trades', 'Health Sciences & Wellness',
                'Social & Behavioral Sciences', 'Science, Engineering, & Math', 'Business, Accounting, & Law',
                'Education & Human Services', 'Exploration & Discovery']
        categorie_list = []
        for i in range(len(self.df)):
            lcp = None
            ed_plan = None
            categorie_list.append(self.df.loc[i, 'Categories'])
            string='  '.join([str(item) for item in categorie_list])
            string = string.split(',')
            for item in string:
                if item in ed_plans:
                    ed_plan = item
                if item in lcps:
                    lcp = item

            if ed_plan == None:
                ed_plan = 'None'
            if lcp == None:
                lcp = 'None'
            return ed_plan, lcp

class ReportGenerator:

    def __init__(self, id, lcp, english_course, math_course):
        id = self.id
        lcp = self.lcp
        english_course = self.english_course
        math_course = self.math_course

    def english_math_dataframe(self):
        headers = ['Student ID', 'LCP', 'English', 'Math']
        lcp_df = pd.DataFrame(columns='headers')
        length = len(lcp_df)
        lcp_df.loc[length, 'Student ID'] = self.student_id
        lcp_df.loc[length, 'LCP'] = self.lcp
        lcp_df.loc[length, 'English'] = self.english_course
        lcp_df.loc[length, 'Math'] = self.math_course




df = pd.read_csv('C:/Users/fmixson/Desktop/Dashboard_files/LCP_English_Math/campus-v2report-enrollment-2023-05-11 (1).csv')
pd.set_option('display.max_columns', None)
df = df[df['Dropped'] == 'No'].reset_index()
id_list = []
for i in range(len(df)):
    if df.loc[i, 'Student ID'] not in id_list:
        id_list.append(df.loc[i, 'Student ID'])

for id in id_list:
    student = MathEnglish(id=id, df=df)
    ed_plan, lcp = student.lcp()
    engl_course, math_course, id = student.English_enrolled()
    print(id)
    report = ReportGenerator(id=id, lcp=lcp, english_course=engl_course, math_course=math_course)
    report.english_math_dataframe()

# df[['First', 'Second', 'Third']] = df.Dropped.str.split(',', expand=True)
# print(df)

