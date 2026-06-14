# TestWaitForMostAllBypass

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostAllBypass(long aValue, unsigned long aTimeout);
```

## Description

Use this function to determine whether the bypass on the MOST hardware connected to the channel has been set to the specified condition within the waiting time. The wait point is only triggered if a change to this condition takes place.

The following can be entered as possible condition values: 1 for closed bypass and 0 for open bypass. In the case of a closed bypass, the MOST device can not be seen by the other devices in the loop.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| 1 | Bypass is closed |
| 0 | Bypass is opened |

## Return Values

-2: Resume based on Constraint Violation

## Availability

| Since Version |
|---|
