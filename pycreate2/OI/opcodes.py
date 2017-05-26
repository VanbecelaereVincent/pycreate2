# Not every opcode is included here becauase they are not all useful.
# For example, no point in scheduling things, a raspberry pi is controlling
# this create 2, I can schedule things on it. There are no brushes installed
# in the create 2 model, so the cleaning modes aren't useful.

RESET = 7
OI_MODE = 35
START = 128
SAFE = 131
FULL = 132
POWER = 133
# SPOT = 134
# CLEAN = 135
# MAX = 136
DRIVE = 137
MOTORS = 138
LED = 139
SONG = 140
PLAY = 141
SENSORS = 142
SEEK_DOCK = 143
MOTORS_PWM = 144
DRIVE_DIRECT = 145
DRIVE_PWM = 146
# STREAM = 148
QUERY_LIST = 149
# PAUSE_RESUME_STREAM = 150
# SCHEDULING_LED = 162
# DIGIT_LED_RAW = 163  # doesn't work
DIGIT_LED_ASCII = 164
# BUTTONS = 165
# SCHEDULE = 167
# SET_DAY_TIME = 168
STOP = 173
