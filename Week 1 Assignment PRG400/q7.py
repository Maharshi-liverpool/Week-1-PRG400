class Counter:
    count = 0 

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()

print("Number of objects created:", Counter.count)
