import os

job_number = int(os.environ['BUILD_NUMBER'])

assert job_number % 3 == 0, "build number are not modulue in 3"
# if job_number % 3 == 0:
print(os.environ['JOB_NAME'])