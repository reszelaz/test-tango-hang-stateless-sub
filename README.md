# Demonstrate hang of Tango client with stateless subscription which fails

Examples to reproduce a Tango client hang when it holds a failing stateless
subscription and destroys `AttributeProxy` object.

In order to reproduce the problem:
1. Register in Tango Database PyDsExp DS with instance name `test` with 1
device of PyDsExp class with the following name: `test/pydsexp/1`
2. Start PyDsExp: `python PyDsExp.py test`
4. Execute client: `python client.py`

The client will hang after a while.
