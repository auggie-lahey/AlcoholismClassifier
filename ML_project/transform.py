import pandas as pd
import numbers
pd.options.mode.chained_assignment =default='warn'
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


# # Read data from dict and csv

# In[2]:

df = pd.read_csv('student-por.csv')
print(df.columns)
df.columns = ['school', 'sex', 'age', 'rural', 'big_family', 'divorced', 'mom_edu', 'dad_edu',
       'mom_job', 'dad_job', 'reason_for_school', 'guardian', 'travel_time', 'study_time',
       'failures', 'extra_school_support', 'extra_family_support', 'paid', 'extracurricular', 'preschool',
       'college', 'internet_access', 'dating', 'home_life', 'free_time', 'party', 'wd_drinker',
       'weekend_drinker', 'health', 'absences', 'fall_grade', 'spring_grade', 'final_grade']
dictionary = pd.read_csv('dict.csv')
dictionary.drop(["Unnamed: 2"], 1)
dictionary['col'] = df.columns


# # Transform data to readable format

# In[3]:

original_data = df.copy()
df = df.replace(['yes', 'no'], [1,0])
df.divorced = df.divorced.replace(["A", "T"], [1,0])
df.big_family = df.big_family.replace(["LE3", "GT3"], [0,1])
df.rural = df.rural.replace(["U","R"], [0,1])
df.sex = df.sex.replace(["M","F"], [0,1])
df.school = df.school.replace(["GP","MS"], [1,2])
df.guardian = df.guardian.replace(["mother","father", "other"], [1,2,3])
df.mom_job = df.mom_job.replace(["teacher","health","services","at_home","other"], [1,2,3,4,5])
df.dad_job = df.dad_job.replace(["teacher","health","services","at_home","other"], [1,2,3,4,5])
df.reason_for_school = df.reason_for_school.replace(["home","reputation", "course","other"], [1,2,3,4])
df['index'] = df.index
df["risk_score"] = df.wd_drinker * df.weekend_drinker


df['school_GP'] = df.school.replace([1,2], [1,0])#["GP","MS"], [1,2])
df['school_MS'] = df.school.replace([1,2], [0,1])

df['guard_mom'] = df.guardian.replace([1,2,3], [1,0,0])#["mother","father", "other"], [1,2,3])
df['guard_dad'] = df.guardian.replace([1,2,3],[0,1,0])#["mother","father", "other"], [1,2,3])
df['guard_other'] = df.guardian.replace([1,2,3], [0,0,1])#["mother","father", "other"], [1,2,3])

#["teacher","health","services","at_home","other"], [1,2,3,4,5])
df['mom_teach'] = df.mom_job.replace([1,2,3,4,5], [1,0,0,0,0])
df['mom_health'] = df.mom_job.replace([1,2,3,4,5], [0,1,0,0,0])
df['mom_service'] = df.mom_job.replace([1,2,3,4,5], [0,0,1,0,0])
df['mom_home'] = df.mom_job.replace([1,2,3,4,5], [0,0,0,1,0])
df['mom_other'] = df.mom_job.replace([1,2,3,4,5], [0,0,0,0,1])

df['dad_teach'] = df.dad_job.replace([1,2,3,4,5], [1,0,0,0,0])
df['dad_health'] = df.dad_job.replace([1,2,3,4,5], [0,1,0,0,0])
df['dad_service'] = df.dad_job.replace([1,2,3,4,5], [0,0,1,0,0])
df['dad_home'] = df.dad_job.replace([1,2,3,4,5], [0,0,0,1,0])
df['dad_other'] = df.dad_job.replace([1,2,3,4,5], [0,0,0,0,1])

#df.reason_for_school = df.reason_for_school.replace(["home","reputation", "course","other"], [1,2,3,4])
df['reason_home'] = df.reason_for_school.replace([1,2,3,4], [1,0,0,0])
df['reason_rep'] = df.reason_for_school.replace([1,2,3,4], [0,1,0,0])
df['reason_course'] = df.reason_for_school.replace([1,2,3,4], [0,0,1,0])
df['reason_other'] = df.reason_for_school.replace([1,2,3,4], [0,0,0,1])


# # Build dictionary for translation

# In[4]:

dictionary.columns = ['original_name', 'meaning', 'classes', 'col']
dictionary = dictionary.replace(np.nan, '', regex=True)
dictionary  = dictionary.set_value(5, 'classes', "1 = divorced")
dictionary  = dictionary.set_value(4, 'classes', "1 = >3")
dictionary  = dictionary.set_value(3, 'classes', "1 = rural")
dictionary  = dictionary.set_value(1, 'classes', "0=male, 1=female")
dictionary  = dictionary.set_value(0, 'classes', "1=GP 1=MS")
dictionary  = dictionary.set_value(11, 'classes', "1=mother, 2=father, 3=other")
dictionary  = dictionary.set_value(8, 'classes', "1=teacher, 2=health 3=services 4=at_home 5=other")
dictionary  = dictionary.set_value(9, 'classes', "1=teacher, 2=health 3=services 4=at_home 5=other")
dictionary  = dictionary.set_value(10, 'classes', "1=close to home, 2=reputation 3=course4 =other")

