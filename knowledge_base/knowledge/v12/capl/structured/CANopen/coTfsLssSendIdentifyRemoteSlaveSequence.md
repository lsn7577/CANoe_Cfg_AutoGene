# coTfsLssSendIdentifyRemoteSlaveSequence

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendIdentifyRemoteSlaveSequence( dword vendorId, dword productCode, dword revNoLowBound, dword revNoHighBound, dword serialNoLowBound, dword serialNoHighBound );
```

## Description

This function sends a LSS identify remote slave sequence.

## Return Values

Error code

## Example

```c
/* sends LSS identify remote slave sequence */

if (coTfsLssSendIdentifyRemoteSlaveSequence( 0x1234, 0x43214321, 0, 0xFFFFFFFF, 0, 1000 ) == 1) {
  /* received LSS identify remote slave sequence, sent response with selected parameters */
}
```
