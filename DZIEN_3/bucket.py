from datetime import datetime,timedelta

#krok 1
class Bucket:
    def __init__(self,period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return f'Bucket(quota = {self.quota})'

bucket = Bucket(60)
print(bucket)

#krok2

def fill(bucket,amount):
    now = datetime.now()
    if (now-bucket.reset_time)>bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount
