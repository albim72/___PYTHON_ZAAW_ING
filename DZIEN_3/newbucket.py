from datetime import datetime, timedelta
from modbucket import fill,deduct

class NewBucket:
    def __init__(self,period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return (f'NewBucket(max_quota = {self.max_quota}, '
                f'quota_consumed = {self.quota_consumed})')

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self,amount):
        delta = self.max_quota - amount
        if amount == 0:
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta

bucket = NewBucket(60)
print(f'początkowo: {bucket}')

fill(bucket,100)
print(f'wypełniono: {bucket}')

if deduct(bucket,99):
    print('potrzebne 99 jednostek')
else:
    print('brak 99 jednostek')

print(f'aktualnie: {bucket}')

if deduct(bucket,3):
    print('potrzebne 3 jednostek')
else:
    print('brak 3 jednostek')

print(f'aktualnie: {bucket}')

