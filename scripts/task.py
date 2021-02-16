from celery_factory import celery

@celery.task(name="random_task_runner")
def execute_runners():
    """
    This is a random task that is supposed to run at any given time
    it can be a ETL script, 
    a script that send mail from a django application or anything you may thing off
    """
    now = datetime.now() - timedelta(days=1)
    print(f"I am running at this time {now}")
