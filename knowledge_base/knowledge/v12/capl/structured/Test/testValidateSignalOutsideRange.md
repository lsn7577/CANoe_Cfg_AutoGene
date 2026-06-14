# testValidateSignalOutsideRange

> Category: `Test` | Type: `function`

## Syntax

```c
long testValidateSignalOutsideRange (char aTestStep[], Signal aSignal, float aLowLimit, float aHighLimit); // form 1
```

## Description

Checks the signal value, the environment variable value or the system variable value against the condition:

The test step is evaluated as passed or failed depending on the results.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| Note Use the int64 parameters for system variables of UInt64 and Int64 type to cover the whole value range. The int64 parameter is interpreted for system variables of UInt64 type as qword (uint64). |  |

## Return Values

-1: General error

## Example

```c
// validates the value of the signal against the given range
long result;
result = testValidateSignalOutsideRange("Check Velocity", Node_SUT::Velocity, 60, 100);
if (result != 0)
TestStepFail("Error occurred!");
```

## Availability

| Since Version |
|---|
