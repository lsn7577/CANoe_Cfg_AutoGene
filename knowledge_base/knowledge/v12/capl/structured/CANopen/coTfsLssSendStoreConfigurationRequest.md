# coTfsLssSendStoreConfigurationRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendStoreConfigurationRequest( byte[] pErrorCode, byte[] pSpecificError );
```

## Description

The function sends a LSS Store Configuration request and waits for the response.

## Return Values

Error code

## Example

```c
byte pErrorCode[1];
byte pSpecificError[1];

/* send LSS store configuration request */

if (coTfsLssSendStoreConfigurationRequest( pErrorCode, pSpecificError) == 1) {
  /* sent LSS store configuration request and received response */
  /* received values can be found in pErrorCode[0], pSpecificError[0] */
}
```
