# Data_Science_Salary_Trends
Modeling of data science salaries for US-based workers in 1Q2023

# Source:  
Kaggle: https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023, accessed 31May2023
aijobs.net
update*** database is updated annualy, last update was updated 2 months ago
Based on updated date as per Kaggle and the date accessed, we assumed the database included data from Jan 2023 to Mar 2023 (1Q2023)
Data are based on user submission of job/salary information.
Original csv: ds_strings.csv

# Tools:
Pandas, Python, Flask, Tableau, Javascript, Scikit-Learn

# Team members:
Calogera McCormick, Aaron Lilleoien, Minta Burke, Sana Ayubzai, Tawn Scotton

# Hypotheses
# Project Parts: Cleaning, Analyis, Modeling, Prediction

# Dataset description
original csv: ds_salaries.csv
CSV includes 11 columns and 3755 rows.
- work_year: The year the salary was paid.
- experience_level: The experience level in the job during the year
- employment_type: The type of employment for the role
- job_title: The role worked in during the year.
- salary: The total gross salary amount paid.
- salary_currency: The currency of the salary paid as an ISO 4217 currency code.
- salaryinusd: The salary in USD
- employee_residence: Employee's primary country of residence in during the work year as an ISO 3166 country code.
- remote_ratio: The overall amount of work done remotely
- company_location: The country of the employer's main office or contracting branch
- company_size: The median number of people that worked for the company during the year

# Dataset refinement
We inspected the csv.
We used Python in a Jupyter notebook (***DataScientistRoles_DSRoles06052023.ipynb) 

The original csv (ds_salaries.csv) was imported into the notebook and refined using Pandas.  Data were limited to preselected parameters.  Variables that were strings were coded to numerical codes to faciliate the machine learning. The job titles were grouped into categories.  Note, there were 93 job titles in the original dataset and this reduced to 44 for roles where the employee resided in the US.
### work_year
work_year was limited to 2023
### experience_level
experience_level (EN, MI, SE, and EX) for entry-level, mid-level, senior-level and executive were coded to 1, 2, 3, and 4, respectively
Codes were stored in a new variable called experience_level_code.
### employment_type
employment_type (CT, FT, and PT) for contractor, full time and part time were coded to 1, 2, and 3
Codes were stored in a new variable called employment_type_code.
### job_title
Job titles were condensed from 44 unique titles to 8 job title categories.  THe job categories are: 
- Data Analyst
- Data Architect
- Data Engineer
- Data Manager
- Data Scientist
- Developer
- Other
- Scientist

The job titles in the DATA ANALYST job_title_category are below.  Code for Data Analyst is 1.
Data Analytics Manager
Business Data Analyst
Data Quality Analyst
Lead Data Analyst
Financial Data Analyst
BI Analyst
Data Analytics Specialist

The job titles in the DATA ARCHITECT job_title_category are below.  Code for Data Architect is 2.
Data Architect
Data Modeler

The job titles in the DATA ENGINEER job_title_category are below.  Code for Data Engineer is 3.
Analytics Engineer
Applied Machine Learning Engineer
BI Data Engineer
Business Intelligence Engineer
Cloud Database Engineer
Computer Vision Engineer
Data Engineer
Data Infrastructure Engineer
Data Operations Engineer
Deep Learning Engineer
Machine Learning Engineer
Machine Learning Infrastructure Engineer
Machine Learning Software Engineer
ML Engineer
MLOps Engineer
NLP Engineer
Research Engineer

The job titles in the DATA MANAGER job_title_category are below.  Code for Data Manager is 4.
Data Manager

The job titles in the DATA SCIENTIST job_title_category are below.  Code for Data Scientist is 5.
Data Scientist
Data Science Manager
Director of Data Science
Machine Learning Scientist
Applied Machine Learning Scientist
Data Science Consultant
Data Science Lead
Data Science Engineer

The job titles in the DEVELOPER job_title_category are below.  Code for Developer is 6.
AI Developer
BI Developer

The job titles in the OTHER job_title_category are below.  Code for Other is 7.
Head of Data
Data Specialist
Head of Data Science
Data Lead

The job titles in the SCIENTIST job_title_category are below.  Code for Scientist is 8.
Applied Scientist
Research Scientist
### salary
The salary column is removed from the refined cav.  THe analysis will be performed on the salary_in_usd field.
### salary_currency
The salary_currency column is removed from the refined cav.  THe analysis will be performed on the salary_in_usd field.
### salary_in_usd
Bins werw created in ranges of 50K USD.  Codes for the salary are 1-8 and are stored in salary_in_usd
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/bb916af9-42df-4615-aead-4d56c55fe942)
### employee_residence
must equal US
### remote_ratio
no edit to the field
### company_location
No change to the field.  After filtering for residence=US and year=2023, all entries in this field were US.  
The salary column is removed from the refined cav. 
### comany_size
company_size (S, M, and L) for small, medium and large were coded to 1, 2, and 3
Codes were stored in a new variable called company_size_code.

### Refined csv: 
DSRoles_US_2023.csv
Number of rows: 1565 rows
Number of columns: 7 (index, employment_type_code, xperience_level_code, job category_code, salary_in_usd_code, company_size_code, remote_ratio)

# limitation
we don't knwo if the salary is salary only or includes other benefits, total compensation or salary only

# Hypotheses - What questions do we plan to answer
- WHat salary can you predict given a job title.  
- What titles can you predict given a salary range
- What job level is predicted based on salary range


# ANALYSES
# Tableau stuff
# MODELING - forest

# learning
initial model was linear regression, however since the y dependent variable was to be predicted into 8 binds or categories, we changed to a forange of rest plot.  The data we aim to predict for salary is categorical, not continuous (eg, range of $101,000 to $150,000, not $123,456)
