import os

job_number = int(os.environ['JOB_NUMBER'])

if job_number % 3 == 0:
    print(os.environ['JOB_NAME'])