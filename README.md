# Demonstrate hang of Tango DS with stateless subscription which fails

Examples to reproduce a Tango DS hang when it holds a failing stateless
subscription and destroys `AttributeProxy` object.

In order to reproduce the problem:
1. Register in Tango Database:
  * PyDsExp DS with instance name `test` with 1 device of PyDsExp class with 
    the following name: `test/pydsexp/1`
  * PyDsExpClient DS with instance name `test` with 1 device of PyDsExpClient 
    class with name: `test/pydsexpclient/1`
2. Start PyDsExp: `python PyDsExp.py test`
3. Start PyDsExpClient: `python PyDsExpClient.py test`
4. Execute client: `python client.py`

The client will exit with `TRANSIENT CORBA timeout` and the `PyDsExpClient` 
will get hang. 
