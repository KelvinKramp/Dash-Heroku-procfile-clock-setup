

**Content**

Mini project for creating a Dash app with a background scheduler in which the time interval of the scheduler can be changed by the Dash input text field. 
Graphical userinterface from Dash can be used to change the frequency of data updates on the Heroku server.  

The procfile has references to three files: 
- line1: "web: something". This is the reference to Dash main app file.
- line2: "worker: something". Reference to the file with the fucntion that does something. 
- line3: "clock: something". This is the reference to the clock file that is supposed to run on the Heroku server continually.

**Sources**

Procfile:
https://pythonhosted.org/deis/using_deis/process-types/#:~:text=A%20Procfile%20is%20a%20mechanism,of%20the%20Twitter%20streaming%20API.
"A Procfile is a text file named Procfile placed in the root of your application that lists the process types in an application. Each process type is a declaration of a command that is executed when a container of that process type is started. All the language and frameworks using Heroku’s Buildpacks declare a web process type, which starts the application server."

Dash basic callback example:
https://dash.plotly.com/basic-callbacks

Apscheduler - Backgroundscheduler (the blockscheduler doesnt allow for job rescheduling at the change of a time_interval variable)
https://apscheduler.readthedocs.io/en/stable/userguide.html

Savind and loading data with JSON:
https://opensource.com/article/19/7/save-and-load-data-python-json
https://www.youtube.com/watch?v=9N6a-VLBa2I&t=22s

Creating a custom clock proces on Heroku:
Scheduled Jobs with Custom Clock Processes in Python with APScheduler
https://devcenter.heroku.com/articles/clock-processes-python
https://medium.com/@gbuszmicz/cron-jobs-in-node-js-with-heroku-5f3c808b4d57

Preventing your dyno from idling and exiting:
https://stackoverflow.com/questions/5480337/easy-way-to-prevent-heroku-idling
https://hackernoon.com/how-to-prevent-your-free-heroku-dyno-from-sleeping-dggxo3bi2


**Dont forget**

- set web_concurrency on 1:
  heroku config:set WEB_CONCURRENCY=1
- scale workers:
  heroku ps:scale clock=1
  
 You can also accomplish it via the Heroku scheduler job (you have to provide your creditcard, but it is free). 
