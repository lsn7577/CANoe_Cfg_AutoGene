# TestJoinFrSymbolEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinFrSymbol ()
```

## Description

Completes the current set of "joined events" with the FlexRay symbol event.

This function does not wait.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| 0 | unknown |
| 1 | CAS |
| 2 | MTS |
| 3 | Wakeup |

## Return Values

-3: Join error

## Availability

| Since Version |
|---|
