# ChkStart_LINHeaderToleranceViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINHeaderToleranceViolation (float Tolerance);
```

## Description

Checks the LIN header transmission time.

An event will be generated, if the measured header transmission time is over specified tolerance.

For a LIN 2.0 compliance the Tolerance has to be in the range [0 .. 40]%.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
...
dword checkId;
// Create and start the check for LIN Header tolerance
checkId = ChkStart_LINHeaderToleranceViolation(40.0, "LINHeaderToleranceCallback");
...
// CAPL callback for violation notification
void LINHeaderToleranceCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
