# ChkStart_LINWakeupReqLengthViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINWakeupReqLengthViolation (duration MinLength, duration MaxLength);
```

## Description

Checks the length of LIN wake-up request.

An event will be generated, if a measured length of the wake-up request is out of the specified range.

According to the LIN specification the wake-up request is a dominant signal in the range of a minimum of 250µs and a maximum of 5ms.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| 0 | Minimum length shall not be checked |
| >0 | Minimum allowed length |

## Example

```c
...
dword checkId;
ChkConfig_SetPrecision(6); // switch to µs precision
// Create and start the check for LIN wake-up request
checkId = ChkStart_LINWakeupReqLengthViolation(250, 1000, "LINWakeupLenCallback");
ChkConfig_SetPrecision(3); // switch to ms precision (default)
...
// CAPL callback for violation notification
void LINWakeupLenCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
