# coTfsLssWaitForSwitchStateSelectiveSequence

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForSwitchStateSelectiveSequence( dword[] pVendorId, dword[] pProductCode, dword[] pRevisionNo, dword[] pSerialNo );
```

## Description

The function waits for a switch state selective messages and sends the response. For a successful test all parameters are to be received within a defined time-out.

## Return Values

Error code

## Example

```c
dword pVendorId[1];
dword pProductCode[1];
dword pRevisionNo[1];
dword pSerialNo[1];

/* waits for LSS switch state selective request */
if (coTfsLssWaitForSwitchStateSelectiveSequence( pVendorId, pProductCode, pRevisionNo, pSerialNo) == 1) {
  /* received LSS switch state selective request */
  /* received values can be found in pVendorId[0], pProductCode[0], pRevisionNo[0], pSerialNo[0] */
}
```
