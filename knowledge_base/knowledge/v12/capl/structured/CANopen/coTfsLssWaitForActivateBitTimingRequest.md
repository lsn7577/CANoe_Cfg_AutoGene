# coTfsLssWaitForActivateBitTimingRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForActivateBitTimingRequest( dword[] pSwitchDelay );
```

## Description

This function waits for LSS Activate Bit-Timings Parameters request.

## Return Values

Error code

## Example

```c
dword pSwitchDelay[1];

/* waits for LSS activate bit timing request */
if (coTfsLssWaitForActivateBitTimingRequest( pSwitchDelay) == 1) {
  /* received LSS activate bit timing request */
  /* received values can be found in pSwitchDelay[0] */
}
```
