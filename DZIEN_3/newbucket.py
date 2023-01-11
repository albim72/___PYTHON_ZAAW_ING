from datetime import datetime, timedelta

class NewBucket:
    def __init__(self,period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0
        
    def __repr__(self):
        return (f'NewBucket(max_quota = {self.max_quota}, '
                f'quota_consumed = {self.quota_consumed}')
