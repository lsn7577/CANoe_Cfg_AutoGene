# TestWaitForSignalInRange

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForSignalInRange (sysvar aSysVar, float aLowLimit, float aHighLimit, dword aTimeout); // form 1
```

## Description

Checks the value of the signal, the system or the environment variable against the condition:

If this condition is already met when this function is called, it returns immediately without waiting.

The test step is evaluated as either passed or failed depending on the results.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Return Values

-1: General error.

## Example

```c
// waits for a specified value range of signal ‘Velocity’
long result;
result = TestWaitForSignalInRange(Velocity, 80, 100, 2000);
```

## Availability

| Since Version |
|---|
