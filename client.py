import time
import PyTango


DEV_NAME = "test/pydsexpclient/1"


def test():
    dp = PyTango.DeviceProxy(DEV_NAME)
    i = 0
    while True:
        print("i = {}".format(i))
        dp.command_inout("Start")
        while dp.State() != PyTango.DevState.ON:
            time.sleep(0.01)
        i += 1


if __name__ == "__main__":
    test()
