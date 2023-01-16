from time import sleep, time, sleep_ms
from pyb import UART
class Snake():
    def __init__(self, inflate, turn_length):
        self.uart = UART(3, 115200)
        self.INFLATE = inflate #time it takes for a chamber to inflate
        #self.LENGTH = length # number of segments the snake have
        self.TURN_LENGTH = turn_length # how many segments should work together for a swirve
                                       #(all curve left, or all curve right)
        self.segments_addr = ["A","B"]# generate addr for each segment
        print(self.segments_addr)
        self.state = [0] * len(self.segments_addr) #state preperation for serpentine
        self.state[0] = -2


    def swirve(self, addr, direct):
        print("segment", addr, "turned", direct)
        self.send(direct, addr=addr)

    def stop(self, addr):
        print("segment", addr, "stopped")

        self.send("S", addr=addr)

    def send(self, cmd, addr):
        self.uart.write(addr)
        self.uart.write(cmd)

    def forward(self,mode="serpentine", reverse=False):
        if mode == 'concertina':
            self.concertina(reverse)
        elif mode == "serpentine":
            self.serpentine(reverse)
        elif mode == "sidewinding":
            self.sidewinding(reverse)
        elif mode == "singular":
            self.singular(reverse)
    def singular(self, reverse):
        self.state=[-1*self.state[0]] * len(self.state)
        self.move(reverse)
    def concertina(self,reverse):
        cnt = 1
        direct = True
        seg_addr = reversed(self.segments_addr) if reverse else self.segments_addr
        for i in reversed(seg_addr):
            self.swirve(i, "L" if direct else "R")
            cnt = cnt + 1 if cnt <= self.TURN_LENGTH else 1
            direct = not direct if cnt == 1 else direct
            sleep(self.INFLATE)
        for i in seg_addr:
            self.stop(i)
            cnt = cnt + 1 if cnt <= self.TURN_LENGTH else 1
            direct = not direct if cnt == 1 else direct
            sleep(self.INFLATE)

    def serpentine(self,reverse=False):
        for j in range(len(self.segments_addr)-1,0,-1):
            self.state[j] = self.state[j-1]
        self.update_head()
        self.move(reverse)

    def move(self,reverse=False):
        actions = reversed(self.state) if reverse else self.state

        for i, seg in enumerate(actions):
            if abs(seg) != 2:
                self.stop(self.segments_addr[i])

            else:
                self.stop(self.segments_addr[i])
                #sleep_ms(500)
                self.swirve(self.segments_addr[i], "L" if seg == -2 else "R")
                #print("swrve")
        #print("slp")
        sleep(self.INFLATE)
        print()
    def update_head(self):
        self.state[0] *= -1
        #if self.state[0] == -2:
            #self.state[0] = 1
        #elif self.state[0] == 1:
            #self.state[0] = 2
        #elif self.state[0] == 2:
            #self.state[0] = -1
        #elif self.state[0] == -1:
            #self.state[0] = -2
    def serpentine_turn(self, direct, reverse=False):
        ori = -2 if direct == "left" else 2
        head = -1 if reverse else 0
        second = 1 if reverse else -2
        while self.state[0] != ori:
            self.serpentine()
        self.serpentine()
        self.state[head] = ori
        self.state[second] = ori
        self.move()

    def sidewinding(self,reverse):
        pass
