# TestWaitForMostSBC

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostSBC(long aValue, unsigned long aTimeout);
```

## Description

The function waits for the expiration of the time aTimeout for the occurrence of the MOST event of a change of the value of the Synchronous Bandwidth Control (SBC) Register.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume based on Constraint Violation

## Availability

| Since Version |
|---|
