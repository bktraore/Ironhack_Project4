import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Users\kyrie\Downloads\Student Mental health.csv")

df.shape
df.info()
stat = df.describe()


df['Dates'] = pd.to_datetime(df['Timestamp']).dt.date
df['Time'] = pd.to_datetime(df['Timestamp']).dt.time
first  = df.pop("Dates")
df.insert(0, 'Dates', first)
second = df.pop("Time")
df.insert(1, 'Time', second)

df = df.drop(['Timestamp'], axis=1)


# remove the spaces at the end of the strings
df['What is your course?'] = df['What is your course?'].str.rstrip()


df[df['Age'].isna()]
df['Age']= df['Age'].replace(np.nan,19)


######
df['What is your course?']= df['What is your course?'].str.capitalize()

df['What is your course?']= df['What is your course?'].replace('Law','Laws')

df['What is your course?']= df['What is your course?'].replace('Diploma nursing','Nursing')
df['What is your course?']= df['What is your course?'].replace('Nursing','Health')
df['What is your course?']= df['What is your course?'].replace('Pharmacy','Health')
df['What is your course?']= df['What is your course?'].replace('Mhsc','Health')
df['What is your course?']= df['What is your course?'].replace('Biomedical science','Health')

df['What is your course?']= df['What is your course?'].replace('Engin','Engine')
df['What is your course?']= df['What is your course?'].replace('Engine','Engineering')

df['What is your course?']= df['What is your course?'].replace('Enm','Laws')

df['What is your course?']= df['What is your course?'].replace('Irkhs','Kirkhs')

df['What is your course?']= df['What is your course?'].replace('Kenms','K Economics and Management sciences')

df['What is your course?']= df['What is your course?'].replace('ALA','Kirkhs')

df['What is your course?']= df['What is your course?'].replace('Koe','Engineering')
df['What is your course?']= df['What is your course?'].replace('Kop','Health')

df['What is your course?']= df['What is your course?'].replace('Benl','English')
df['What is your course?']= df['What is your course?'].replace('Diploma tesl','English')

df['What is your course?']= df['What is your course?'].replace('Econs','Economics')

df['What is your course?']= df['What is your course?'].replace('Bcs','Banking studies')

df['What is your course?']= df['What is your course?'].replace('Bit','It')

df['What is your course?']= df['What is your course?'].replace('Kirkhs','Islamic education')
df['What is your course?']= df['What is your course?'].replace('Pendidikan islam','Islamic education')
df['What is your course?']= df['What is your course?'].replace('Usuluddin','Islamic education')
df['What is your course?']= df['What is your course?'].replace('Fiqh fatwa','Islamic education')
df['What is your course?']= df['What is your course?'].replace('Fiqh','Islamic education')



######
df['Your current year of Study']= df['Your current year of Study'].str.capitalize()

# replace year by value between 1-4
df['Your current year of Study']= df['Your current year of Study'].replace('Year 1',1)
df['Your current year of Study']= df['Your current year of Study'].replace('Year 2',2)
df['Your current year of Study']= df['Your current year of Study'].replace('Year 3',3)
df['Your current year of Study']= df['Your current year of Study'].replace('Year 4',4)
######
df['What is your CGPA?']= df['What is your CGPA?'].replace('3.50 - 4.00 ','3.50 - 4.00')

df['What is your CGPA?']= df['What is your CGPA?'].replace('0 - 1.99',1)
df['What is your CGPA?']= df['What is your CGPA?'].replace('2.00 - 2.49',2)
df['What is your CGPA?']= df['What is your CGPA?'].replace('2.50 - 2.99',3)
df['What is your CGPA?']= df['What is your CGPA?'].replace('3.00 - 3.49',3)
df['What is your CGPA?']= df['What is your CGPA?'].replace('3.50 - 4.00',4)


###### replace yes - no by 1 and 0 in 3 columns
df[['Do you have Depression?','Do you have Anxiety?','Do you have Panic attack?','Did you seek any specialist for a treatment?','Marital status']]=df[['Do you have Depression?','Do you have Anxiety?','Do you have Panic attack?','Did you seek any specialist for a treatment?','Marital status']].replace('Yes',1)
df[['Do you have Depression?','Do you have Anxiety?','Do you have Panic attack?','Did you seek any specialist for a treatment?','Marital status']]=df[['Do you have Depression?','Do you have Anxiety?','Do you have Panic attack?','Did you seek any specialist for a treatment?','Marital status']].replace('No',0)


df_missing = df.isna().sum().sort_values(ascending=False)
for i in df.columns: 
    print(df[i].unique())
    
#
print(df.duplicated())
df.drop_duplicates(inplace = True)

df.info()




#df.to_csv(r"C:\Users\kyrie\ironhack\project4\cleansheet2.csv")

