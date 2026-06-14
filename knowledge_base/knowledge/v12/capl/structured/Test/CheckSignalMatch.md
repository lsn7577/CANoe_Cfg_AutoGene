# CheckSignalMatch

> Category: `Test` | Type: `function`

## Syntax

```c
long CheckSignalMatch(Signal aSignal, float aCompareValue); // form 1
```

## Description

Checks the given value against the value of signal, the system or the environment variable. The resolution of the signal is considered.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Return Values

1: If the condition is TRUE

## Example

```c
// checks if the value of the signal matches a specified value
long result;
result = CheckSignalMatch(Node_SUT::Velocity, 80);
if (result != 1)
TestStepFail("Value of signal matches not the value ‘80’!");
```

## Availability

| Since Version |
|---|
