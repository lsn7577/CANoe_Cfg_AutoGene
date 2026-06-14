# checkSignalInRange

> Category: `Test` | Type: `function`

## Syntax

```c
long checkSignalInRange(Signal aSignal, float aLowLimit, float aHighLimit); // form 1
```

## Description

Checks the signal value or the environment variable value or the system variable value against the condition:

aLowLimit <= Value <= aHighLimit

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Return Values

1: If the condition is TRUE

## Example

```c
// checks if the value of the signal is in the given range
long result;
result = checkSignalInRange(Node_SUT::Velocity, 60, 100);
if (result != 1)
TestStepFail("Value of signal is not in the allowed range!");
```

## Availability

| Since Version |
|---|
