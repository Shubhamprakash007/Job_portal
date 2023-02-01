# API Docs and Workflow

## Different API endpoints that you require for the app

1. **`POST /register_employer`**: This endpoint will allow employers to create a new account.
2. **`POST /register_student`**: This endpoint will allow job seekers to create a new account.
3. **`POST /login_student`**: This endpoint will allow job seekers to login into their account.
4. **`POST /login_employer`**: This endpoint will allow employers to login into their account.
5. **`POST /resume`**: This endpoint will allow job seekers to post their resume.
6. **`POST /jobpost`**: This endpoint will allow employers to post a job.
7. **`GET /success`**: This endpoint will display a success message.
8. **`POST /apply/<int:job_id>`**: This endpoint will allow job seekers to apply for a job.
9. **`GET /logout_student`**: This endpoint will allow job seekers to logout of their account.
10. **`GET /logout_employer`**: This endpoint will allow employers to logout of their account.
11. **`GET /`**: This endpoint will direct to the home page.
12. **`GET /account`**: The "@login_required" decorator ensures that only logged-in users can access the endpoint, as accessing this endpoint requires authentication..
12. **`GET /about`**: This endpoint will show details about the website.
13. **`GET /view_apply`**: This endpoint will show applications to employer for a particilar job.

## Individual API input parameters and response formats

Here are the API endpoints with the input parameters and response formats in the code:

1. /register_employer

Input: Employer Registration Form data (username, email, password)
Output:
On success: A flash message saying "Account created for [username]!" and a redirect to the employer login page.
On failure: Renders the register_employer.html template with the form.

2. /register_student

Input: Student Registration Form data (username, email, password)
Output:
On success: A flash message saying "Account created for [username]!" and a redirect to the student login page.
On failure: Renders the register_student.html template with the form.

3. /login_student

Input: Student Login Form data (email, password)
Output:
On success: Login the student and redirect to the home page with a flash message.
On failure: Renders the login_student.html template with the form.

4. /login_employer

Input: Employer Login Form data (email, password)
Output:
On success: Login the employer and redirect to the jobpost page with a flash message.
On failure: Renders the login_employer.html template with the form.

5. /resume

Input: Resume Form data (name, email, objective, experience, education, skills)
Output:
On success: Adds the resume data to the database and redirect to the success page.
On failure: Renders the resume.html template with the form.

6. /jobpost

Input: Job data (job_title, company_name, location, job_description, salary=form, experience_required, employer_id)
Output:
On success: Adds the job post data to the database and redirect to the
success page. 
On failure: Renders the job post.html template with the form.

7. /apply/<int:job_id>

Input: Job data (job_title, company_name, location, job_description, salary=form, experience_required, employer_id)
Output:
On success: Adds the job post data to the database and redirect to the
success page. 
On failure: Renders the job post.html template with the form.


## API doc including all the endpoints and input params and response formats

[Link Text](routes.py)

## API workflow diagram

![API Diagram.jpeg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/32c28995-96c4-4293-8636-ab188dd5fea2/API_Diagram.jpeg)

