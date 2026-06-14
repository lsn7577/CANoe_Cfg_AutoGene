# ChkStart_LINETFViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINETFViolation (dword ETFFrameId, char[] CaplCallback);
```

## Description

Checks the format of a single response to ETF. An event will be generated, if the first data byte does not match protected ID of any of the associated frames (Slave failure).

Checks the collision resolution process. An event will be generated during collision resolution, if one of the following is detected:

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
...
dword checkId;
// Create and start the check for LIN Event-triggered frame
// Parameters: Frame identifier of event-triggered frame to verify and optional CAPL 
// callback
checkId = ChkStart_LINETFViolation (0x3A, "CallbackLINETFViolation"); 
...
// CAPL callback for violation notification
void CallbackLINETFViolation (dword aCheckId)
{
ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
