
# coding: utf-8

# # Import libs

# In[1]:

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
pd.set_option('display.max_colwidth', -1)


# In[5]:

#make sure all columns are numerical
for col in df.columns:
    if not(isinstance(df[col][0], numbers.Integral)):
        print(col)


# In[6]:

bins=np.arange(0, 6)
x =plt.hist(df.wd_drinker,facecolor ='red', alpha=.5, bins=bins)
y =plt.hist(df.weekend_drinker,facecolor ='blue',alpha=.3, bins=bins)
plt.style.use('fivethirtyeight')
plt.style.use('ggplot') 
plt.show()
print(x[0])
print(y[0])


# In[7]:

face = []
for i in df.index:
    face.append((df.iloc[i].weekend_drinker,df.iloc[i].wd_drinker))
letter_counts = Counter(face)
no = pd.DataFrame.from_dict(letter_counts, orient='index')
x=[]
y=[]
s=[]
no.columns = ["tuples"]
for i in range(len(no.index)):
    x.append(no.index[i][0])
    y.append(no.index[i][1])
    s.append(5000*no.tuples[i]/241)
plt.scatter(x, y, s)
plt.xlim(0,6)
plt.ylim(0,6)
plt.xlabel("we_response", fontsize=15)
plt.ylabel("wd_response", fontsize=15)
plt.title('Boozin Dist')
plt.grid(True)
plt.show()


# # Potential metrics and distributions

# In[20]:

df["we*wd"] = df.wd_drinker * df.weekend_drinker
df["wd/we"] = df.wd_drinker / df.weekend_drinker
df["we/2twd/5"] = df.wd_drinker/5 + df.weekend_drinker/2
df["wetwd"] = df.wd_drinker + df.weekend_drinker
df["2wdtwe"] = 2*df.wd_drinker + df.weekend_drinker

handles = ["we + wd", "2wd + we", "we * wd", "wd/we","we/2 + we/5"]
binwidth = .05
bins=np.arange(0, 3.5, .05)

plt.hist(df["wetwd"], normed=1,facecolor ='blue', alpha =.7)
plt.hist(df["2wdtwe"], normed=1,facecolor ='black', alpha =.7)
plt.grid(True)
plt.legend(handles[0:2])
plt.show()
plt.hist(df["we*wd"],normed=1, facecolor='yellow', alpha=.75)
plt.grid(True)
plt.legend(handles[2:3])
plt.show()
plt.xlim(0,3)
plt.hist(df["wd/we"], normed=True, facecolor ='green', alpha =.7)#, bins=bins)
plt.hist(df["we/2twd/5"],normed=True,facecolor ='red', alpha =.7)#, bins=bins)
plt.grid(True)
plt.legend(handles[3:])
plt.show()


# # Label data 

# In[9]:

#https://www.sciencedaily.com/releases/2010/05/100531190855.htm
#http://www.who.int/substance_abuse/publications/global_alcohol_report/profiles/prt.pdf
#prolly should label top 10% as high risk, and bottom 60 as no risk.
metric = ['wetwd']
l0 = df.sort_values(metric, ascending=[1])[-65:]
l1 = df.sort_values(['wetwd'], ascending=[1])[390:600]
l2 = df.sort_values(['wetwd'], ascending=[1])[:390]
labels = ['high_risk', 'low_risk', 'no_risk']
ls = []
for r in range(len(df)):
    if df.loc[r]['index'] in l0.index:
        ls.append(labels[0])
    elif df.loc[r]['index'] in l1.index:
        ls.append(labels[1])
    elif df.loc[r]['index'] in l2.index:
        ls.append(labels[2])
    else: 
        print('something went wrong')
        
df['label'] = ls
print(labels[0] +': '+ str(len(df.loc[df.label == labels[0]])))
print(labels[1] +': '+ str(len(df.loc[df.label == labels[1]])))
print(labels[2] +': '+ str(len(df.loc[df.label == labels[2]])))


# # Seperate training data and test data randomly

# In[10]:

test = df.sample(n=round(len(df)/3), replace=False,random_state=6)
train = df[~df.index.isin(test.index)]
print(len(train)+ len(test))


# In[ ]:



