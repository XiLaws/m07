import numpy as np
import pandas as pd
sal = pd.read_csv('Salaries.csv')
sal.head()
sal.info()
sal['BasePay'].mean()
sal['OvertimePay'].max()
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]
sal[sal['TotalPayBenefits']  == sal['TotalPayBenefits'].min()]
sal.groupby('Year').mean()['BasePay']
sal['JobTitle'].nunique()
grouped = sal.groupby('JobTitle').count()
top5 = grouped.sort_values(by='Id',  ascending=False)[:5]
top5['Id']
copied_sal = sal[sal['Year'] == 2013]
group = copied_sal.groupby('JobTitle').count()
count = group[group['Id'] == 1]
count.count()['Id']
def find_chief(job_title):    
    if 'chief' in job_title.lower().split():
        return True
    else:
        return False

sal = pd.read_csv('Salaries.csv')

sum(sal['JobTitle'].apply(lambda x: find_chief(x)))
sal['title_len'] = sal['JobTitle'].apply(len)

sal[['title_len', 'TotalPayBenefits']].corr()