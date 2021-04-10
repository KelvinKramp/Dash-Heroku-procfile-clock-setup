Mini project for creating a Dash app with a background scheduler in which the time interval of the scheduler can be changed by the Dash input text field. 
Graphical userinterface from Dash can be used to change the frequency of data updates on the Heroku server.  

The procfile has references to three files: 
- line1: "web: something". This is the reference to Dash main app file.
- line2: "worker: something". Reference to the file with the fucntion that does something. 
- line3: "clock: something". This is the reference to the clock file that is supposed to run on the Heroku server continually.

Dash basic callback example:
https://dash.plotly.com/basic-callbacks

I used the following sources:
Apscheduler - Backgroundscheduler (the blockscheduler doesnt allow for job rescheduling at the change of a time_interval variable)
https://apscheduler.readthedocs.io/en/stable/userguide.html

Savind and loading data with JSON:
https://opensource.com/article/19/7/save-and-load-data-python-json
https://www.youtube.com/watch?v=9N6a-VLBa2I&t=22s

Creating a custom clock proces on Heroku:
Scheduled Jobs with Custom Clock Processes in Python with APScheduler
https://devcenter.heroku.com/articles/clock-processes-python

Dont forget to:
- set web_concurrency on 1:
  heroku config:set WEB_CONCURRENCY=1
- scale workers:
  heroku ps:scale clock=1
- start Heroku scheduler job (you have to provide your creditcard, but it is free). Place following command to run in the job:
  python clock.py


