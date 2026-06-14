# ChkStart_LINDiagDelayTimesViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINDiagDelayTimesViolation (Node ObservedNode);
```

## Description

Checks the values of P2_min and ST_min for a specified LIN Slave node or for all LIN Slaves defined in LDF.

An event will be generated, if the measured P2_min or ST_min value is smaller than one specified in the database (LDF).

The check monitors bus traffic and automatically recognizes diagnostic frames.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
...
dword checkId;
// Create and start the check for LIN diagnostic delay times
checkId = ChkStart_LINDiagDelayTimesViolation("LINDiagDelayTimesCallback"); 
...
// CAPL callback for violation notification
void LINDiagDelayTimesCallback (dword aCheckId)
{   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
