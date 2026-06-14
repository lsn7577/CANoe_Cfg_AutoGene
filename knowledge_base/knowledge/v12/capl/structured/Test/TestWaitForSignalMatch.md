# TestWaitForSignalMatch

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForSignalMatch (Signal aSignal, float aCompareValue, dword aTimeout); // form 1
```

## Description

Checks the given value against the value of the signal, the system variable or the environment variable. The resolution of the signal is considered.

If this condition is already met when this function is called, it returns immediately without waiting.

The test step is evaluated as either passed or failed depending on the results.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Return Values

-1: General error

## Example

```c
// waits for a specified value of signal ‘Velocity’
long result;
result = TestWaitForSignalMatch(Node_SUT::Velocity, 80, 1000);
```

## Availability

| Since Version |
|---|
