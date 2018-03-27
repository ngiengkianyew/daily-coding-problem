from time import sleep

def sample_function():
    print("hello")

def schedule_function(f, delay_in_ms):
    delay_in_s = delay_in_ms / 1000
    sleep(delay_in_s)
    f()

schedule_function(sample_function, 10000)
