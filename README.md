

**Dash app with background scheduler for Heroku**

Mini project for creating a Dash app with a background scheduler in which the time interval of the scheduler can be changed by the Dash input text field. 
The text input field from Dash can be used to change the frequency of data updates on the Heroku server.  

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
Medium post
https://medium.com/@gbuszmicz/cron-jobs-in-node-js-with-heroku-5f3c808b4d57

Preventing your dyno from idling and exiting:
https://stackoverflow.com/questions/5480337/easy-way-to-prevent-heroku-idling
https://hackernoon.com/how-to-prevent-your-free-heroku-dyno-from-sleeping-dggxo3bi2


**Options to make the app working**
There are three options for getting the clock-file running:
1) Create a connection of the frontend dash app with the background clock through "from clock import job" and then run the job in de dash python file main.py through a thread on the background. A webpage in Heroku will idle after 30 minutes if there are no visitors, so the clock will stop after 30 min. if there are no visitors. You can pay and change this or in this case you can also use another third party that pings your website to keep the website from idling. Someone made a Heroku app for doing the latter which can be found in this link: http://kaffeine.herokuapp.com/
2) Create a Scheduler job in Heroku. Click on Resources within your app and in the textfield of add-ons fill in scheduler. Start a Scheduler. You have to give your creditcard number, but you won't be charged if you don't go over the limit. You can check the limit with the command heroku ps. Abbreviations are soms hard to deciver in the coding world, but I think the ps stands for process. In my case this option gave me problems, it was hard to set my clock scheduling according to a specific interval. The Scheduler works well, but is not very accurate.  
3) Create a clock proces (https://devcenter.heroku.com/articles/clock-processes-python). To do this you have to create a Procfile (stands for Process file, https://devcenter.heroku.com/articles/procfile). The Procfile contains three lines of code that reference to three files: 
- line1: "web: gunicorn dash_app_name:server". This is the reference to Dash main app file. Gunicorn is the Web Server Gateway Interface (WSGI) HTTP server, I think this is a complex piece of code that makes it possible for a request of your url to get referred to your working Dash app. 
- line2: "worker: python do_something.py". Reference to the file with the fucntion that does something. 
- line3: "clock: python clock.py". This is the reference to the clock file that is supposed to run on the Heroku server continually.
In this option if you want to start your clock you have to do it manually with the command "heroku ps:scale clock=1". This command runs line 2 in the Procfile. This third option is probably the most professional and flexibel one. The problem I had over with this is that you can only implement a limited amount of dyno as a free user. The web app is started automatically after your pushed your repository with git. If you also run your clock you have no other options such as running an CLI (command line interface). So eventually I choose for the first option. 

If you see your app running twice at every scheduled run this could be caused by two things: 
1) You need to set your web_concurrency to 1:
  heroku config:set WEB_CONCURRENCY=1
2) You need to set your debugging mode to False at the end of your dash app file. 
  
