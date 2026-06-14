# coTfsLssSendFastScanRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendFastScanRequest( dword idNumber, dword bitCheck, dword sub, dword next );
```

## Description

This function sends a LSS fast scan protocol request.

## Return Values

Error code

## Example

```c
/* send LSS fast scan protocol request */

if (coTfsLssSendFastScanRequest(0x000002, 28, 1, 1) == 1) {
  /* request sent */
}
```
