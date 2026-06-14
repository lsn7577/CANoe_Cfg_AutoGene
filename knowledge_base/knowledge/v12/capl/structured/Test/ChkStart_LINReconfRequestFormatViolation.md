# ChkStart_LINReconfRequestFormatViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINReconfRequestFormatViolation ();
```

## Description

Checks the format of LIN reconfiguration requests.

An event will be generated, if in a detected reconfiguration request at least one Slave attribute is violated.

As reconfiguration request considered frames with ID=0x3C, carrying the Service Identifier byte (SID) in the range [0xB0..0xB7]

Checked attributes: NAD, supplier ID, function ID, variant ID, message ID, protected ID, StartIndex.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
...
dword checkId;
// Create and start the check for LIN reconfiguration request format violation
checkId = ChkStart_LINReconfRequestFormatViolation("LINReconfRequestFormatCallback"); 
...
// CAPL callback for violation notification
void LINReconfRequestFormatCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
