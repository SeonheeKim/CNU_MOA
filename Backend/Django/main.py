import crawlings
import schedule
import time

schedule.every(3).seconds.do(crawlings.run)
while True:
    schedule.run_pending()
    time.sleep(1)
