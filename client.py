import time
import threading
import PyTango


DEV_NAME = "test/pydsexp/1"


class JobThread(threading.Thread):

    def __init__(self):
        super(JobThread, self).__init__()

    def run(self):
        attr = PyTango.AttributeProxy(DEV_NAME + "/attr1")
        attr.write(10)


def test():
    dp = PyTango.DeviceProxy(DEV_NAME)
    dp.subscribe_event("attr2", PyTango.EventType.CHANGE_EVENT,
                       PyTango.utils.EventCallback(), [], True)
    i = 0
    while True:
        print("i = {}".format(i))
        thread = JobThread()
        thread.start()
        while thread.isAlive():
            time.sleep(0.01)
        i += 1


if __name__ == "__main__":
    test()
