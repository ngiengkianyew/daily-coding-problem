from time import time
from random import random, randrange
import bisect

REQUESTS_PER_FILE = 100


class PersistedFile:
    # in a memory efficient implementation, this would be persisted to disk
    # once full and only the path and metadata would remain in memory
    def __init__(self):
        self.start_timestamp = None
        self.end_timestamp = None
        self.request_timestamps = list()

    def __repr__(self):
        return "start={}, end={}, size={}".format(
            self.start_timestamp, self.end_timestamp, len(self.request_timestamps))


class RequestQuery:
    def __init__(self):
        self.current_file = PersistedFile()
        self.prev_files = list()

    def record(self, timestamp):
        if not self.current_file.start_timestamp:
            self.current_file.start_timestamp = timestamp
        self.current_file.request_timestamps.append(timestamp)
        self.current_file.end_timestamp = timestamp

        if len(self.current_file.request_timestamps) == REQUESTS_PER_FILE:
            self.prev_files.append(self.current_file)
            self.current_file = PersistedFile()

    def total(self):
        return (len(self.prev_files) * REQUESTS_PER_FILE) + \
            len(self.current_file.request_timestamps)

    def range(self, lower, upper):
        all_files = self.prev_files + [self.current_file]
        start_times = [x.start_timestamp for x in all_files]
        end_times = [x.end_timestamp for x in all_files]

        start_file_index = bisect.bisect_left(start_times, lower) - 1
        end_file_index = bisect.bisect_left(end_times, upper)
        start_file = all_files[start_file_index]
        end_file = all_files[end_file_index]

        start_file_pos = bisect.bisect(start_file.request_timestamps, lower)
        end_file_pos = bisect.bisect(end_file.request_timestamps, upper)

        num_req = 0
        num_req += len(start_file.request_timestamps[start_file_pos:])
        num_req += len(end_file.request_timestamps[:end_file_pos])
        num_req += (end_file_index - start_file_index) * REQUESTS_PER_FILE

        return num_req


def run_experiments(requests):
    rq = RequestQuery()
    lower, upper = None, None

    for i in range(requests):
        rq.record(i)

        if random() < 0.001:
            if not lower:
                lower = i
            else:
                upper = randrange(lower, i)

            if lower and upper:
                num_req = rq.range(lower, upper)
                print("{} requests made between {} and {}".format(
                    num_req, lower, upper))
                print("Total: {}".format(rq.total()))
                lower, upper = None, None


run_experiments(112367)
