# coTfsLssWaitForFastScanRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForFastScanRequest( dword[] pId, byte[] pBitCheck, byte[] pSub, byte[] pNext );
```

## Description

This function waits for the Fast Scan message.

## Return Values

Error code

## Example

```c
dword pId[1];
byte  pBitCheck[1];
byte  pSub[1];
byte  pNext[1];

/* waits for the fast scan request */
if (coTfsLssWaitForFastScanRequest( pId, pBitCheck, pSub, pNext ) == 1) {
  /* request received */
  /* received values can be found in pId, pBitCheck, pSub, pNext */
}
```
