# TestJoinJ1939PGEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinJ1939PGEvent (dbMessage aMessage)
```

## Description

Completes the current set of joined events with the transmitted event.This function does not wait.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-3: Join error

## Example

```c
// add J1939 PG event to the current set of “joined events” and fill the parameter group data to parameter group ‘eventMessage’

pg TSC1 pgTSC1;
dword index = 0;
TestJoinJ1939PGEvent (TSC1);
// ... other join events
index = TestWaitForAllJoinedEvents (2000);

TestGetWaitJ1939PGData (index, pgTSC1);
```

## Availability

| Since Version |
|---|
