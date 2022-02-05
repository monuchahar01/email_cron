from apscheduler.schedulers.background  import BlockingScheduler
from run import sendMail
sched = BlockingScheduler()


def maina():
    """Run tick() at the interval of every ten seconds."""
   
    sched.add_job(sendMail, 'interval', minutes=2)
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass 


maina()
