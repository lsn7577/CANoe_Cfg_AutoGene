# TestGetWaitJ1939PGData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitJ1939PGData (pg * aPG); // form 1
```

## Description

If a J1939 parameter group event is the last event that triggers a wait instruction, the message content can be called up with the first function.

The second function can only be used for joined events. The number of the joined event (return value of testJoin...) is here being used as an index.

## Return Values

0: Data access successful.

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
