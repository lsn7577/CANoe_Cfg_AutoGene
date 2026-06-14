# TestWaitForFrNullFrame

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForFrNullFrame (dbFrFrame aFrame, dword aTimeout);
```

## Description

Waits for the occurrence of the specified FlexRay Null Frame. Should the event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no Null Frame is specified the wait condition is resolved on any FlexRay Null Frame.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Availability

| Since Version |
|---|
