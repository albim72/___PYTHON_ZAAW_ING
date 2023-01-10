class PostiveNumberTuple(tuple):
    def __new__(cls, *numbers):
        skipped_val = 0
        positive = []
        for x in numbers:
            if x>=0:
                positive.append(x)
            else:
                skipped_val+=1
        instance = super().__new__(cls,tuple(positive))
        instance.skipped_val = skipped_val
        return instance


pos = PostiveNumberTuple(9,0,-4,5,7,12,-3,0,-44,2,4,-1,23,5)
print(type(pos))
print(pos)
print(pos.skipped_val)
