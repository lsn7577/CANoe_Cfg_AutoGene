# coTfsLssSendConfigureBitTimingResponse

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendConfigureBitTimingResponse( dword errorCode, dword specificError );
```

## Description

This function sends the LSS Configure Bit-Timings Parameters response.

## Return Values

Error code

## Example

```c
/* send LSS configure bit timing response with error code and specific error = 0*/

if (coTfsLssSendConfigureBitTimingResponse( 0, 0 ) != 1) {
  /* message could not be sent */
}
```
