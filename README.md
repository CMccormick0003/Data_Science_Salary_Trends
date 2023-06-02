# Data_Science_Salary_Trends
Modeling of data science salaries for US-based workers in 1Q2023

# Source:  
Kaggle: https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023, accessed 31May2023
aijobs.net
update*** database is updated annualy, last update was updated 2 months ago
Based on updated date as per Kaggle and the date accessed, we assumed the database included data from Jan 2023 to Mar 2023 (1Q2023).
Assumption - data are based on user submission of job/salary information

# Tools:
Pandas, Python, Flask, Tableau, Javascript, Scikit-Learn

# Team members:
Calogera McCormick, Aaron Lilleoien, Minta Burke, Sana Ayubzai, Tawn Scotton

# Refinement of the dataset
We inspected the csv.
CSV includes 11 columns
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

We used Python in a Jupyter notebook (***ADD NAME HERE) 

- to reduce the dataset to include only row for employees residing in the US 
- to limit rows to job postings to year 2023
- 
dsroles_us_2023
