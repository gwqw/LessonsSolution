"""
    Buffer has size.
    Input: buff size (number packets it can hold) and number of packets
          pak1: arrival1 duration1, arival2 duration2
    if buff is full then it discards next packet (returns -1).
    else it put packet to buffer and treat them duration time

    Ex.1:
    1 0
    out: # no packet -> no output

    Ex.2:
    1 1
    0 0
    out: 0 # start to treat at time 0

    Ex.3:
    1 2
    0 1
    0 1
    out: 0
    -1 # buffer is full, so it discard the packet

    Ex.4:
    1 2
    0 1
    1 1
    out:
    0
    1
"""

INF = 1e7

class Queue:
    def __init__(self, max_size):
        self.data = []
        self.max_size = max_size

    def push(self, element):
        self.data.append(element)

    def pop(self):
        element = self.data[0]
        self.data = self.data[1:]
        return element

    def first(self):
        return self.data[0]

    def empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

class Packet:
    def __init__(self, arival, duration):
        self.arival = arival
        self.duration = duration

def getPackOut(q, ai):
    for i in range(q.size()):
        p = q.first()
        if p.arival + p.duration <= ai:
            q.pop()
        else:
            break

def treat_packets(pack_list, max_size):
    output = []
    q = Queue(max_size)
    et = 0
    for p in pack_list:
        ai, di = p.arival, p.duration
        getPackOut(q, ai)
        if q.size() < max_size:
            oi = max(ai, et)
            q.push(Packet(oi, di))
            output.append(oi)
            et = oi + di
        else:
            output.append(-1)
    return output

def test_example():
    # example 1
    pack_list = []
    max_size = 1
    output = treat_packets(pack_list, max_size)
    assert(output == [])

    # example 2
    pack_list = [Packet(0, 0)]
    max_size = 1
    output = treat_packets(pack_list, max_size)
    assert(output == [0])

    # example 3
    pack_list = [Packet(0, 1), Packet(0, 1)]
    max_size = 1
    output = treat_packets(pack_list, max_size)
    assert(output == [0, -1])

    # example 4
    pack_list = [Packet(0, 1), Packet(1, 1)]
    max_size = 1
    output = treat_packets(pack_list, max_size)
    assert(output == [0, 1])

    # example 5
    pack_list = [Packet(1, 1), Packet(1, 2),Packet(1, 3),]
    max_size = 2
    output = treat_packets(pack_list, max_size)
    assert(output == [1, 2, -1])

    # example 6
    pack_list = [Packet(0, 0), Packet(0, 0), Packet(0, 0),
                 Packet(1, 0), Packet(1, 0), Packet(1, 1),
                 Packet(1, 2),Packet(1, 3),]
    max_size = 2
    output = treat_packets(pack_list, max_size)
    assert(output == [0, 0, 0, 1, 1, 1, 2, -1])

if __name__ == "__main__":
    test_example()
    max_size, pack_num = (int(s) for s in input().split())
    pack_list = []
    for i in range(pack_num):
        arrival, duration = (int(s) for s in input().split())
        pack_list.append(Packet(arrival, duration))
    output = treat_packets(pack_list, max_size)
    for o in output:
        print(o)
    
