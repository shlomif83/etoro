import os

job_number = int(os.environ['BUILD_NUMBER'])


def print_job_name():
    assert job_number % 3 == 0, "build number is not % in 3"
    print("job name is:" + os.environ['JOB_NAME'])

if __name__ == "__main__":
    print_job_name()