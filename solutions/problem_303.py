from math import isclose

FLOAT_EQUALITY_TOLERANCE = 0.5


def get_angle_for_hour(hour: int, minute: int):
    minute_offset = minute / 12
    hour_angle = (hour * 30) + minute_offset
    return hour_angle


def get_angle_for_minute(minute: int):
    return minute * 6


def get_angle(hhmm_time: str):
    hour, minute = map(int, hhmm_time.split(":"))
    hour %= 12
    ha = get_angle_for_hour(hour, minute)
    ma = get_angle_for_minute(minute)

    angle = abs(ha - ma)
    return angle if angle < 180 else 360 - angle


# Tests
assert isclose(get_angle("12:20"), 118, abs_tol=FLOAT_EQUALITY_TOLERANCE)
assert isclose(get_angle("12:00"), 0, abs_tol=FLOAT_EQUALITY_TOLERANCE)
assert isclose(get_angle("6:30"), 3, abs_tol=FLOAT_EQUALITY_TOLERANCE)
assert isclose(get_angle("3:45"), 176, abs_tol=FLOAT_EQUALITY_TOLERANCE)
