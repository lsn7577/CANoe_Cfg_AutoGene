# coTfsLssSendInquireProductCodeRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendInquireProductCodeRequest( dword[] pProductCode );
```

## Description

This function sends an Inquire product code request and waits for the response.

## Return Values

Error code

## Example

```c
dword pProductCode[1];

/* send LSS inquire product code request */

if (coTfsLssSendInquireProductCodeRequest( pProductCode ) == 1) {
  /* sent LSS inquire product code request and received response */
  /* received value can be found in pProductCode */
}
```
