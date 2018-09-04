import sys

ENTER = "enter"
EXIT = "exit"


def get_busiest_slot(events):
    ts_entries, ts_exits = dict(), dict()
    max_time, min_time = -sys.maxsize, sys.maxsize

    for event in events:
        ts_dict = None
        timestamp = event["timestamp"]
        if event["type"] == ENTER:
            ts_dict = ts_entries
        else:
            ts_dict = ts_exits

        ts_dict[timestamp] = event["count"]
        if timestamp < min_time:
            min_time = timestamp
        elif timestamp > max_time:
            max_time = timestamp

    people_inside = 0
    max_people_inside = 0
    start_time, end_time = None, None
    for timestamp in range(min_time, max_time + 1):
        if timestamp in ts_entries:
            people_inside += ts_entries[timestamp]
            if people_inside > max_people_inside:
                max_people_inside = people_inside
                start_time = timestamp
        if timestamp in ts_exits:
            if people_inside == max_people_inside:
                end_time = timestamp
            people_inside -= ts_exits[timestamp]

    return (start_time, end_time)


# Tests
events = [
    {"timestamp": 1526579928, "count": 3, "type": "enter"},
    {"timestamp": 1526579982, "count": 4, "type": "enter"},
    {"timestamp": 1526580054, "count": 5, "type": "exit"},
    {"timestamp": 1526580128, "count": 1, "type": "enter"},
    {"timestamp": 1526580382, "count": 3, "type": "exit"}
]
assert get_busiest_slot(events) == (1526579982, 1526580054)
