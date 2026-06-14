# ChkStart_LINRespErrorSignal

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINRespErrorSignal (Node ObservedNode);
```

## Description

Checks the LIN Response_Error signal for a specified LIN Slave node or for all LIN nodes.

An event will be generated, if the Response_Error signal value changes from FALSE (0) to TRUE (1).

J2602 specific: Bit 7 of Status Byte serves as Response_Error signal.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
...
dword checkId;
// Create and start the check for LIN response_error signal
checkId = ChkStart_LINRespErrorSignal("LINRespErrCallback"); 
...
// CAPL callback for violation notification
void LINRespErrCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
