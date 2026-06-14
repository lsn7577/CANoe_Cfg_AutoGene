# coTfsSDOWaitForAbortCode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOWaitForAbortCode( dword nodeID );
```

## Description

This function waits until either a SDO abort message was received by the selected DUT Device Under Test or a time-out has occurred. After this, the abort code can be read out with coTfsSDOGetAbortCode.

## Return Values

Error code

## Example

```c
if ( coTfsSDOWaitForAbortCode (2) == 1) {
  write("SDO abort message received, use coTfsSdoGetAbortCode to retrieve its data");
}
```
