from time import sleep
class Snake():
    def __init__(self):
        self.segments_addr = [0x09,0x08,0x07,0x06,0x05,0x04,0x03,0x02]
        self.state = [0] * len(self.segments_addr)
        print(self.state)
        self.TURN_LENGTH = 1
        self.INFLATE = 1.2
        self.state[0] = -2
    def concertina(self,reverse=False):
        cnt = 1
        direct = True
        seg_addr = reversed(self.segments_addr) if reverse else self.segments_addr

        for i in seg_addr:
            self.swirve(i, "L" if direct else "R")
            cnt = cnt + 1 if cnt < self.TURN_LENGTH else 1
            direct = not direct if cnt == 1 else direct
            sleep(self.INFLATE/len(self.segments_addr))

        for i in reversed(seg_addr):
            self.stop(i)
            cnt = cnt + 1 if cnt < self.TURN_LENGTH else 1
            direct = not direct if cnt == 1 else direct
            sleep(self.INFLATE/(len(self.segments_addr)+1))
    def draw(self, reverse=False):
        actions = reversed(self.state) if reverse else self.state
        print("\n"*5)
        print(actions)
        for i in actions:
            if i == -2:
                print("@| |")
            elif i == 2:
                print(" | |@")
            else:
                print(" |@|")
        print("\n")
        sleep(0.25)
    def swirve(self, addr, direct):
        print(addr, direct)
    def stop(self, addr):
        print(addr, "S")

snake = Snake()
for i in range(1):
    snake.concertina()
#snake.concertina_turn("right")
#for i in range(10):
    #snake.concertina()
