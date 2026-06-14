# ChkCreate_AllNodesBabbling, ChkStart_AllNodesBabbling

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_AllNodesBabbling (Duration aMinQuietTime, char [] CaplCallback);
```

## Description

There is a time interval where transmissions are tolerated. After the interval has been passed, all nodes may no longer send messages. From now on, each transmission of the nodes is reported.

If the min. quiet time is 0, then each message sent by any node leads to the event.

Possible application: Supervises the end of a communication. Supervises the transition of nodes’ or buses’ state to "sleep active".

Gateway nodes require that the bus context corresponds to the network that is being observed.

For FlexRay only valid data frames and PDUs are recognized as communication, Null Frames and Erroneous frames are ignored.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks that after 300 ms no transmission are available
checkId = ChkStart_AllNodesBabbling(300);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
