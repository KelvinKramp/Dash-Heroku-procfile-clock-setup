from apscheduler.schedulers.background import BackgroundScheduler
import os
import json

# THIS IS THE HIGH LEVEL FUNCTION FOR BACKGROUND JOB
def job():
    # initiate BackgroundScheduler
    sched = BackgroundScheduler()
    sched.start()

    # read time_interval variable from json file
    time_interval_file_path = os.path.join("time_interval.json")
    with open(time_interval_file_path, "r") as time_interval_file:
        read_file = time_interval_file.read()
        data = json.loads(str(read_file))
    # read variable from the json file and define as time_int1
    global time_int
    time_int = int(data["TIME-INTERVAL"])

    # THIS IS THE LOW LEVEL FUNCTION FOR BACKGROUND JOB, THIS FUNCTION WILL RUN ACCORDING TO THE TIME_INTERVAL VARIABLE
    # FROM THE JSON FILE
    def timed_job():
        # read variable again from the json file and define as time_int2
        time_interval_file_path = os.path.join("time_interval.json")
        with open(time_interval_file_path, "r") as time_interval_file:
            read_file = time_interval_file.read()
            data = json.loads(str(read_file))
        time_int2 = int(data["TIME-INTERVAL"])
        print("read time interval from json file, time interval = ", time_int2)
        global time_int
        print("old time interval =", time_int)
        sched.print_jobs()
        # if changed than reschedule job en restart with new variable
        if time_int2 != time_int:
            print("time interval setting changed... rescheduling job")
            new_time = '*/'+str(time_int2)
            job = sched.reschedule_job('my_job_id', trigger='cron', second=new_time)
            print("job rescheduled with time interval", time_int2)
            time_int = time_int2
        else:
            print("running job every", time_int, "seconds")

    # schedule job with time interval variable
    sched.add_job(timed_job, 'interval', seconds=time_int, id='my_job_id')

