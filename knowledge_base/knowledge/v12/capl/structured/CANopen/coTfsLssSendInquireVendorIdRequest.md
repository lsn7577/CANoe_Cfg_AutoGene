# coTfsLssSendInquireVendorIdRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendInquireVendorIdRequest( dword[] pVendorId );
```

## Description

The function sends an Inquire vendor-ID request and waits for the response.

## Return Values

Error code

## Example

```c
dword pVendorId[1];

/* send LSS inquire vendor ID request */

if (coTfsLssSendInquireVendorIdRequest( pVendorId ) == 1) {
  /* sent LSS inquire vendor ID request and received response */
  /* received value can be found in pVendorId[0] */
}
```
