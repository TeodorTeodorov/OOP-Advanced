class Time:
    max_hours = 23
    max_minute = 59
    max_second = 59
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds  = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds +=1
        if self.seconds > self.max_second:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > self.max_minute:
                self.minutes = 0
                self.hours += 1
                if self.hours > self.max_hours:
                    self.hours = 0

        return self.get_time()

time = Time(10, 59, 59)

print(time.next_second())