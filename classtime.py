class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.normalize()

    def normalize(self):
        self.minute += self.second // 60
        self.second %= 60
        self.hour += self.minute // 60
        self.minute %= 60
        self.hour %= 24

    def __add__(self, other):
        return Time(
            self.hour + other.hour,
            self.minute + other.minute,
            self.second + other.second
        )

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


t1 = Time(10, 45, 50)
t2 = Time(2, 30, 20)

t3 = t1 + t2

print(t3)
