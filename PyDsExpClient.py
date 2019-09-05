import sys
import time
import threading

import PyTango


DEV_NAME = "test/pydsexp/1"


class JobThread(threading.Thread):

    def __init__(self, dev=None):
        super(JobThread, self).__init__()
        self.dev = dev

    def run(self):
        attr = PyTango.AttributeProxy(DEV_NAME + "/attr1")
        attr.write(10)
        self.dev.set_state(PyTango.DevState.ON)


class PyDsExpClientClass(PyTango.DeviceClass):

    cmd_list = {'Start': [[PyTango.ArgType.DevVoid, ""],
                          [PyTango.ArgType.DevVoid, ""]]}

    def __init__(self, name):
        PyTango.DeviceClass.__init__(self, name)
        self.set_type("TestDevice")


class PyDsExpClient(PyTango.Device_4Impl):

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self, cl, name)
        self.info_stream('In PyDsExpClient.__init__')
        PyDsExpClient.init_device(self)

    @PyTango.DebugIt()
    def init_device(self):
        self._stop_flag = False
        self._thread = None
        self._dp = PyTango.DeviceProxy(DEV_NAME)
        self._id = self._dp.subscribe_event("attr2",
                                            PyTango.EventType.CHANGE_EVENT,
                                            PyTango.utils.EventCallback(),
                                            [], True)
        self.set_state(PyTango.DevState.ON)

    @PyTango.DebugIt()
    def delete_device(self):
        if self._thread:
            self._thread.join()
        self._dp.unsubscribe_event(self.id_)

    @PyTango.DebugIt()
    def is_Start_allowed(self):
        return self.get_state() == PyTango.DevState.ON

    @PyTango.DebugIt()
    def Start(self):
        while self._thread and self._thread.isAlive():
            time.sleep(0.01)
        self.set_state(PyTango.DevState.MOVING)
        self.debug_stream('Starting thread...')
        self._thread = JobThread(self)
        self._thread.start()


if __name__ == '__main__':
    util = PyTango.Util(sys.argv)
    util.add_class(PyDsExpClientClass, PyDsExpClient)

    U = PyTango.Util.instance()
    U.server_init()
    U.server_run()
