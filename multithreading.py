#  multithreading = used to perform multiple tasks concurrently (multitasking)
#  good for I/O bound tasks like reading files or fetching data from APIs
#  threading. Thread(target=my_function)

import threading
import time 

def walk_dog(name):
    time.sleep(4)
    print(f"you finish walk the dog {name}")

def take_out_trash():
    time.sleep(2)
    print("you take out trash")

def get_mail():
    time.sleep(4)
    print("you get the mail")


# walk_dog()
# take_out_trash()
# get_mail()

# comma = , is necessary in args as we passing the tuple
chore1 = threading.Thread(target=walk_dog, args=("Scooby",))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target = get_mail)
chore3.start()

# if we do join methods print will happen after all the functions
chore1.join()
chore2.join()
chore3.join()

print("all chores are done")