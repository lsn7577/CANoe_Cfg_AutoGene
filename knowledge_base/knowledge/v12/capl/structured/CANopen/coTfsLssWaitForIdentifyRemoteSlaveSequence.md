# coTfsLssWaitForIdentifyRemoteSlaveSequence

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForIdentifyRemoteSlaveSequence( dword[] pVendorId, dword[] pProductCode, dword[] pRevNoLowBound, dword[] pRevNoHighBound, dword[] pSerialNoLowBound, dword[] pSerialNoHighBound );
```

## Description

This function waits for a LSS identify remote slave sequence.

For a successful test all parameters are to be received within a defined time-out.

## Return Values

Error code

## Example

```c
dword pVendorId[1];
dword pProductCode[1];
dword pRevNoLowBound[1];
dword pRevNoHighBound[1];
dword pSerialNoLowBound[1];
dword pSerialNoHighBound[1];

/* waits for a LSS identify remote slave sequence */
if (coTfsLssWaitForIdentifyRemoteSlaveSequence( pVendorId, pProductCode, pRevNoLowBound, pRevNoHighBound, pSerialNoLowBound,pSerialNoHighBound ) == 1) {
  /* waits for LSS identify remote slave sequence */
  /* received values can be found in pVendorId, pProductCode, pRevNoLowBound, pRevNoHighBound, pSerialNoLowBound,pSerialNoHighBound */
}
```
