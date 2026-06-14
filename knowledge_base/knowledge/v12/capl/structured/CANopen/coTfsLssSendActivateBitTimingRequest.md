# coTfsLssSendActivateBitTimingRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendActivateBitTimingRequest( dword switchDelay );
```

## Description

This function sends a LSS Activate Bit-Timing Parameter request.

## Return Values

Error code

## Example

```c
/* send LSS activate bit timing protocol request */

if (coTfsLssSendActivateBitTimingRequest( 1000) != 1) {
/* message could not be sent */
}
```
