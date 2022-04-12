def test_sequence():
    num = 0
    while num<10:
        yield num
        num += 1
for i in test_sequence():
       print(i, end=",")