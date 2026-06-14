# coTfsLssWaitForConfigureBitTimingRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForConfigureBitTimingRequest( byte[] pTableSelector, byte[] pTableIndex );
```

## Description

This function waits for LSS Configure Bit-Timings Parameters request.

## Return Values

Error code

## Example

```c
byte pTableSelector[1];
byte pTableIndex[1];

/* waits for LSS configure bit timing request */
if (coTfsLssWaitForConfigureBitTimingRequest( pTableSelector, pTableIndex) == 1) {
  /* received LSS configure bit timing request */
  /* received values can be found in pTableSelector[0], pTableIndex[0] */
}
else {
  /* no request received */
  return;
}
```
