# coTfsSDOWaitForSpecificAbortCode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOWaitForSpecificAbortCode( dword nodeId, dword sdoAbortCode );
```

## Description

The function waits for receiving the specified SDO abort message of the device or the occurrence of a time-out.

## Return Values

Error code

## Example

```c
dword nodeId = 0x5;

if (coTfsSDOWaitForSpecificAbortCode(nodeId, sdoAbortCode) == 1) {
  write("SDO abort message received");
}
```
