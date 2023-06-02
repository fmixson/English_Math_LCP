import pandas as pd
import openpyxl


class MathEnglish:
    def __init__(self, id, student_df):
        self.id = id
        self.student_df = student_df

    def English_enrolled(self):
        english_course = None
        math_course = None
        math_courses = ['MATH-104', 'MATH-110A', 'MATH-112', 'MATH-112S', 'MATH-114', 'MATH-116', 'MATH-140']
        english_courses = ['ENGL-100', 'ENGL-100S']
        for i in range(len(self.student_df)):
            if self.student_df.loc[i, 'Course Number'] in english_courses:
                english_course = self.student_df.loc[i, 'Course Number']

            if self.student_df.loc[i, 'Course Number'] in math_courses:
                math_course = self.student_df.loc[i, 'Course Number']

        if english_course == None:
            english_course = 'None'
        if math_course == None:
            math_course = 'None'
        return english_course, math_course, self.id


class LCPsEdplans:

    def __init__(self, student_df):
        self.student_df = student_df

    def lcp(self):
        # head_count_df = self.df.drop_duplicates(subset='Student ID').reset_index
        ed_plans = ['ASEP: Abbreviated Educational Plan', 'CSEP: Comprehensive Educational Plan']
        lcps = ['Arts, Humanities, & Communication', 'Applied Technology & Skilled Trades',
                'Health Sciences & Wellness',
                'Social & Behavioral Sciences', 'Science, Engineering, & Math', 'Business, Accounting, & Law',
                'Education & Human Services', 'Exploration & Discovery']
        categorie_list = []
        for i in range(len(self.student_df)):
            lcp = None
            ed_plan = None
            categorie_list.append(self.student_df.loc[0, 'Categories'])
            string = '  '.join([str(item) for item in categorie_list])
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

    def __init__(self, id, lcp, ed_plan, english_course, math_course, dataframe):
        self.id = id
        self.lcp = lcp
        self.ed_plan = ed_plan
        self.english_course = english_course
        self.math_course = math_course
        self.lcp_df = dataframe

    def english_math_dataframe(self):
        length = len(lcp_df)
        self.lcp_df.loc[length, 'Student ID'] = self.id
        self.lcp_df.loc[length, 'LCP'] = self.lcp
        self.lcp_df.loc[length, 'Ed Plan'] = self.ed_plan
        self.lcp_df.loc[length, 'English'] = self.english_course
        self.lcp_df.loc[length, 'Math'] = self.math_course
        return lcp_df


columns = ['Student ID', 'LCP', 'Ed Plan', 'English', 'Math']
lcp_df = pd.DataFrame(columns=columns)
df = pd.read_csv(
    'C:/Users/fmixson/Desktop/Dashboard_files/LCP_English_Math/campus-v2report-enrollment-2023-05-23(3).csv')

pd.set_option('display.max_columns', None)
df = df[df['Dropped?'] == 'No'].reset_index()
id_list = []
for i in range(len(df)):
    if df.loc[i, 'Student ID'] not in id_list:
        id_list.append(df.loc[i, 'Student ID'])

for id in id_list:
    student_df = df[df['Student ID'] == id]
    student_df = student_df.reset_index()
    student = MathEnglish(id=id, student_df=student_df)
    engl_course, math_course, id = student.English_enrolled()
    lcpedplans = LCPsEdplans(student_df=student_df)
    ed_plan, lcp = lcpedplans.lcp()

    print('English:', engl_course, 'Math:', math_course, id)
    report = ReportGenerator(id=id, lcp=lcp, ed_plan=ed_plan, english_course=engl_course, math_course=math_course,
                             dataframe=lcp_df)
    lcp_df = report.english_math_dataframe()
    print(lcp_df)
lcp_df.to_excel('EM_df.xlsx')
# df[['First', 'Second', 'Third']] = df.Dropped.str.split(',', expand=True)
# print(df)
