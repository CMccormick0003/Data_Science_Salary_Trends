# Data Scientist Salary Predictor
# Scope:  
Build a model to predict data science salaries for US-based workers in 1Q2023.  Build an app to use the model for predictions.  
Provide a resource for those who who work in data sciences and those that are entering the field to have knowledge of the current landscape trends.
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/6a1a94ff-e425-48b1-a7ad-74bd083730fa)

# Source:  
Kaggle: https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023, accessed 31May2023. 

Based on updated date as per Kaggle and the date accessed, we assumed the database included data from Jan 2023 to Mar 2023 (1Q2023).
Data are based on self user submission of job/salary information to aijobs.net.  The original csv is ds_strings.csv.

#  Packages:
Pandas, Python (Path, Flask, pickle), Tableau, Scikit-Learn, Matplotlib, HTML, CSS, PowerPoint, Microsoft csv, GitHub

# Team members:
Calogera McCormick, Aaron Lilleoien, Minta Burke, Sana Ayubzai, Tawn Scotton

# Project Parts: Cleaning, Analyis, Modeling, Prediction

# Cleaning
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

### Summary of Data Volume per Step
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/120b60eb-4d6a-4bd4-acdf-30fadd8a7e21)
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/4b6901bf-1023-4d0b-8887-36af7cf875fa)

# Dataset refinement
We inspected the csv.
We used Python in a Jupyter notebook (***DataScientistRoles_DSRoles06052023.ipynb) 

The original csv (ds_salaries.csv) was imported into the notebook and refined using Pandas.  Data were limited to preselected parameters.  Variables that were strings were coded to numerical codes to faciliate the machine learning. The job titles were grouped into categories.  Note, there were 93 job titles in the original dataset and this reduced to 44 for roles where the employee resided in the US.

### Count of Job Titles in Original Dataset
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/ece7b5f7-ad0e-4255-8b44-638f76795250)

### work_year
work_year was limited to 2023
### experience_level
experience_level (EN, MI, SE, and EX) for entry-level, mid-level, senior-level and executive were coded to 1, 2, 3, and 4, respectively
Codes were stored in a new variable called experience_level_code.
### employment_type
employment_type (CT, FT, and PT) for contractor, full time and part time were coded to 1, 2, and 3
Codes were stored in a new variable called employment_type_code.
### job_title
Job titles were condensed from 44 unique titles to 6 job title categories.  THe job categories are: 
- Data Analyst
- Data Engineer
- Analytics Engineer
- Machine Learning Role
- Data Scientis
- Data Architect

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

### Data Analysis
### Average salary per job title (original dataset)
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/6cfa9fd0-1514-4cef-92d8-20aee2eb8cb3)

### Bivariate analysis of the refined dataset to investiagte which fewatures to include in the model.
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/3f178139-3c47-4d53-9eca-58ff58af07a8)

Tableau was used in a variety way to look at the data which preparing both models.  The app includes links to Tableau Public with visualizations of data from th original dataset and the model.

### Building the model
Model accuracy was under 20% with the refined csv.  This was perfomred with logistic regression and a forest model.  Several modifications were made and the final forest model used 6 job titles and 4 bins for salary.  The features were reduced to 4 (job title, experience level, remote ratio and company size).  
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/37d92687-cf7f-410c-99ac-4de4f634648c)
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/acdf530f-cb19-4245-9348-e31e9f6468e4)
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/600e3cb6-cd13-4d95-b92a-bee39fc1d75b)

![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/13d52c15-5b75-4ab6-b330-9203d81f24d9)

Model used 35% of data from the original dataset.  .  
The model can predict a salary given four inputs (level of experience, job tile, remote percentage and company size)?  All inputs are codes.

# Learnings from Building and Training the Model
initial model was linear regression, however since the y dependent variable was to be predicted into 8 binds or categories, we changed to a forest plot.  The data we aim to predict for salary is categorical, not continuous (eg, range of $101,000 to $150,000, not $123,456)

THe model was run several ways.  To work on improving accuracy of the model, we modified the model parameters by revising the grouping or revising which fields to include.  For example, the model was run with 8 categories for salaries in 50 K increments from 1 as <=50K USD to 8 as >=350K USD to be 4 categories in 100 K increments (1 as <= 100 K USD to 4 as >= 301K USD).  

Another modification was shifting from 9 categories for job title (Data Analyst, Data Architect, Data Engineer, Data Manager, Data Scientist, Developer, Other, and Scientist) to be 7 categories (Data Analyst, Data Architect, Data Engineer, Data Manager, Data Scientist, Developer, Other) by combining Data Scientist and Scientist into one category.  Furhter the job titles were reduced to 6, only the most common jobs in the dataset (data analyst, data engineer, analytics engineer, machine learning engineer, data scientist and data architect).  The only job title that is a combination of roles in the model is the ML role.

# Web Development
Flask and HTML were used to develop an app that runs in the development environment.
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/f03f177c-cf5e-467b-8c82-b6f7d8f920ac)
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/f5e81443-d314-4643-be42-b6200dac80f7)
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/fa2c409d-196d-4e48-b5eb-58370718fad3)
### Sample Salary Predictions
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/3bcec812-f7fe-4bb4-9117-ad26a30c5be2)

# Limitations
It is unclear if the reported salary in the dataset is total compensation or solely salary.  Time in position was not available so it is not known if the salary for that level of experience if for a person new to the position or someone who has been in it a long time.  To help users of the model predictor, an educational page was added to the app to describe what additional features are part of total compensation that they should consider.

### Data Sources:
Original dataset:  https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023
Figures in the app:  Index.html:  https://unsplash.com/photos/mcSDtbWXUZU, Results.html:  https://unsplash.com/photos/xuTJZ7uD7PI and https://cdn.pixabay.com/photo/2015/06/19/21/24/avenue-815297_1280.jpg
Figures in the presentation: Introduction slide: https://unsplash.com/photos/klMii3cR9iI, App Navigation slide:  https://unsplash.com/photos/oWrRxo9UdM4, Know your worth slide: https://unsplash.com/photos/-8a5eJ1-mmQ and https://unsplash.com/photos/5ZnS3wK6sUg, Data Sources slide:  https://unsplash.com/photos/64YrPKiguAE, Questions slide: https://unsplash.com/photos/IgUR1iX0mqM, 
![image](https://github.com/CMccormick0003/Data_Science_Salary_Trends/assets/120672518/a3fac443-4c81-40aa-9744-8aa855543140)
