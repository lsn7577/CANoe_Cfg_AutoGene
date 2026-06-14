# ChkStart_LINRespToleranceViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINRespToleranceViolation (Message Frame, float Tolerance);
```

## Description

Checks the LIN response transmission time.

An event will be generated, if the measured response transmission time is over allowed tolerance.

This function monitors frames transmitted without a failure only

Components influencing response tolerance: inter-byte space, response space

For a LIN 2.0 compliance the Tolerance has to be in the range [0 .. 40]%.

## Example

```c
...
dword checkId;
ChkConfig_SetPrecision(9); // switch to ns precision
// Create and start the check for LIN response tolerance violation in “Motor1” node
checkId = ChkStart_LINRespToleranceViolation(LIN20db::Motor1, 40.0 , "LINRespToleranceCallback");
ChkConfig_SetPrecision(3); // switch to ms precision (default)
...
// CAPL callback for violation notification
void LINRespToleranceCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
