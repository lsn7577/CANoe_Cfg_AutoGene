# coTfsLssSendConfigureNodeIdRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendConfigureNodeIdRequest( dword NID, byte[] pErrorCode, byte[] pSpecificError );
```

## Return Values

Error code

## Example

```c
byte pErrorCode[1];
byte pSpecificError[1];

/* send LSS configure nodeID request and wait for response */

if (coTfsLssSendConfigureNodeIdRequest( 112 , pErrorCode, pSpecificError) == 1) {
  /* request sent and DUT replied with correct response. Response values can be found in pErrorCode, pSpecificError */
}
```
