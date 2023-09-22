def infinite_count():
    num = 1
    while True:
        yield num
        num += 1

count = infinite_count()
for _ in range(5):
    print(next(count))
    
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator to count down from 5
for number in countdown(5):
    print(number)
