# TestWaitForMostAsRegistry

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMostAsRegistry(long aRegistry, unsigned long aTimeout);
```

## Description

The function waits for the specified time period for any change to a registry in the application socket.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| 1 | Wait for changes in the local registry |
| 2 | Wait for changes in the global registry |
| -1 | Wait for changes in all registries |

## Return Values

-2: Resume based on Constraint Violation

## Availability

| Since Version |
|---|
