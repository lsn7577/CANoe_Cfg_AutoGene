# TestGetWaitFrPOCStateData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitFrPOCStateData (FrPOCState aPOCState);
```

## Description

If an event indicating a change of state on the FlexRay Communication Controller's protocol operation state machine is the last event that triggers a wait instruction, the event’s content can be called up with the first function.

The second function can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

## Return Values

0: Data access successful

## Availability

| Since Version |
|---|
