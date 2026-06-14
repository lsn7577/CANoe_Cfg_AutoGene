# ChkCreate_MostNetState, ChkStart_MostNetState

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostNetState(long aOldState, long aNewState);
```

## Description

This check is used to monitor the NetState state of the MOST hardware interface.

Concrete checks can be implemented for any NetState state changes, and are triggered when a NetState event having the corresponding target state occurs with a specified initial state.

The wildcard value –1 can be specified for one of the netstate parameters, if the check should monitor only the beginning or ending of a netstate. Both parameters can be set to wildcard value, if the check should detect any occurring netstate change.

This check always works on events. Therefore, it will not detect a current netstate, that has been established before the time of the check’s activation, as a new netstate.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: Check could not be created and must not be referenced

## Availability

| Since Version |
|---|
