MAX_TIME = 5400

class MicrowaveBase:
    time = 0;

    def set_time(self, minutes, seconds):
        self.time = 60 * minutes + seconds

    def inc_time(self, time):
        self.time += time
        if self.time > MAX_TIME: self.time = MAX_TIME

    def dec_time(self, time):
        self.time -= time
        if self.time < 0: self.time = 0

    def show_time(self):
        #print("show_time: ", self.time)
        minutes = self.time // 60
        seconds = self.time - minutes*60
        return "%02d:%02d" % (minutes, seconds)    

class Microwave1(MicrowaveBase):
    def show_time(self):
        res = super().show_time()
        res = '_' + res[1:]
        return res

class Microwave2(MicrowaveBase):
    def show_time(self):
        res = super().show_time()
        res = res[:-1] + '_'
        return res

class Microwave3(MicrowaveBase):
    pass

class RemoteControl:
    def __init__(self, micro_wave):
        self.micro_wave = micro_wave

    def set_time(self, time):
        minutes, seconds = time.split(':')
        minutes = int(minutes)
        seconds = int(seconds)
        self.micro_wave.set_time(minutes, seconds)

    def add_time(self, time):
        if time[-1] == 's':
            self.micro_wave.inc_time(int(time[:-1]))
        elif time[-1] == 'm':
            self.micro_wave.inc_time(60 * int(time[:-1]))
        else:
            print("Something goes wrong")

    def del_time(self, time):
        if time[-1] == 's':
            self.micro_wave.dec_time(int(time[:-1]))
        elif time[-1] == 'm':
            self.micro_wave.dec_time(60 * int(time[:-1]))
        else:
            print("Something goes wrong")

    def show_time(self):
        return self.micro_wave.show_time()


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")
    
    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    print("1. ", remote_control_1.show_time())
    print("2. ", remote_control_2.show_time())
    print("3. ", remote_control_3.show_time())
    
    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")
