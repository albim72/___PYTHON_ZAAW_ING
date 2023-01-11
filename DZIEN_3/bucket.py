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

#krok3

def deduct(bucket,amount):
    now = datetime.now()
    if (now-bucket.reset_time)>bucket.period_delta:
        return False #wiadro nie zostało napełnione
    if bucket.quota - amount < 0:
        return False #wiadro zostało napełnione częściowo
    bucket.quota -= amount
    return True #wiadro zostało napełnione

fill(bucket, 100)
print(bucket)

if deduct(bucket, 99):
    print('potrzebne 99 jednostek danych')
else:
    print('nie ma 99 jednostek')

print(bucket)

if deduct(bucket, 3):
    print('potrzebne 3 jednostki danych')
else:
    print('nie ma 3 jednostek')

print(bucket)
