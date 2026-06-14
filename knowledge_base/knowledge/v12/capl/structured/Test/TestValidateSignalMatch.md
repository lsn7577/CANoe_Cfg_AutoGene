# TestValidateSignalMatch

> Category: `Test` | Type: `function`

## Syntax

```c
long TestValidateSignalMatch (char aTestStep[], Signal aSignal, float aCompareValue); // form 1
```

## Description

Checks the given value against the value of the signal, the system variable or the environment variable. The resolution of the signal is considered.

The test step is evaluated as either passed or failed depending on the results.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Return Values

0: Correct functionality

## Example

```c
// validates the value of the signal against the given value
long result;
result = TestValidateSignalMatch("Check Velocity", Node_SUT::Velocity, 80);
```

## Availability

| Since Version |
|---|
