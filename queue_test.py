import queue

# FIFO(First-In, First-Out) 또는 LILO(Last-In, Last-Out) 방식
data_queue = queue.Queue()
data_queue.put(1)
data_queue.put(2)  # 1 - 2
data_queue.put(3)  # 1 - 2 - 3
print(data_queue.get())  # 1 출력
print(data_queue.get())  # 2 출력
print(f"qsize : {data_queue.qsize()}")
