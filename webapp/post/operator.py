from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from .views.postRank import PostRank


def start():
    scheduler=BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    @scheduler.scheduled_job('cron', second=23, name = 'check')
    def auto_check():
        post = PostRank()
        print(f"-------{post}-------")
    scheduler.start()