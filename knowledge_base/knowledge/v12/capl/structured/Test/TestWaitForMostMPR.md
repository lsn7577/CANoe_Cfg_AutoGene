# TestWaitForMostMPR

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostMPR(long aValue, unsigned long aTimeout);
```

## Description

The function waits until the expiration of the time aTimeout for the occurrence of the MOST event of a change of the Maximum Position Registers (MPR).

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume based on Constraint Violation

## Availability

| Since Version |
|---|
