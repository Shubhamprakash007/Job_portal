# The Backend and DB Design Planning

## Fundamental entities of the job portal

1. Employer/Company - represents a company that posts job listings
2. Job Seeker - represents an individual who is looking for employment
3. Job Listing - represents a job posting made by an employer
4. Application - represents an application made by a job seeker for a specific job listing
5. Skills - represent the skills required for a specific job listing
6. Resume/Profile - represent the job seeker's educational and professional background. 

## Data points collected from the user

1. Personal Information: name, email and password
2. Resume/CV: name, email, objective, experience, education and skills
3. Employer Information: name, email, and password.
4. Job Information: job title, company name, location, job description, salary, experience required, and employer id.

## Backend workflow for the app

1. User Registration: A user can register on the job portal website by providing basic personal information, and contact details, and creating a password.
2. User Login: The user can log in to the job portal using the registered email and password.
3. Job Search: Users can search for jobs by specifying the job title, location, and other relevant filters.
4. Job Application: Users can apply for a job by submitting their resume and cover letter.
5. Employer Dashboard: Employers can access their dashboard to post job openings and view job applications.
6. Resume Management: Users can upload their resumes to the job portal and make them visible to employers.
7. Data Storage: All user and job data will be securely stored in a database.
8. API Integration: The job portal's backend will expose APIs to allow integration with other job-related services, such as resume builders or career assessment tools.

## Create an ERD diagram of your database using dbdiagram.io

![ERD.png]https://github.com/Shubhamprakash007/Job_portal/blob/main/job_portal/static/ERD.png