# Etoro exercise

## Description

This project is consists of three stages.
* first Jenkins job(pull-code) to get source code from GitHub repo https://github.com/shlomif83/etoro.git .
* second Jenkins job(run-script) is to execute a Python script that prints Jenkins job name only one from three times.
* third Jenkins job(print-first-job-number) to print the job number of the first job.

## Getting Started
1. nevigate to Jenkins server http://40.113.21.164. If that doesn't work, use RDP to connect to the server and navigate to http://loclalhost

![image](https://user-images.githubusercontent.com/34093578/97117547-1f2d2c80-170d-11eb-93c2-0cb2dfba19ae.png)

2. enter username and password and click sign in.
3. select first job(pull-code).

![image](https://user-images.githubusercontent.com/34093578/97117588-661b2200-170d-11eb-8be1-667e2996af27.png)
4. click build now and track after logs.

![image](https://user-images.githubusercontent.com/34093578/97117624-995db100-170d-11eb-9b70-9d457f2d47a4.png)
