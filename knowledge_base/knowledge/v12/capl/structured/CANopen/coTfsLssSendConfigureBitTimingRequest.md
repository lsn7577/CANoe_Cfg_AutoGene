# coTfsLssSendConfigureBitTimingRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendConfigureBitTimingRequest( dword tableSelector, dword tableIndex, byte[] pErrorCode, byte[] pSpecificError );
```

## Description

This function sends a LSS Configure Bit-Timings Parameters request and waits for the response.

## Return Values

Error code

## Example

```c
byte pErrorCode[1];
byte pSpecificError[1];

/* send LSS configure bit timing request and wait for reponse*/

if (coTfsLssSendConfigureBitTimingRequest( 0, 3, pErrorCode, pSpecificError) == 1) {
  /* request sent with parameters tableSelector=0 and tableIndex=3 and DUT replied with correct response. Response values can be found in pErrorCode, pSpecificError */
}
```
