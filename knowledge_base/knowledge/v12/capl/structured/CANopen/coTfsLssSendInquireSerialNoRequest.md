# coTfsLssSendInquireSerialNoRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendInquireSerialNoRequest( dword[] pSerialNo );
```

## Description

This function sends an Inquire serial number request and waits for the response.

## Return Values

Error code

## Example

```c
dword pSerialNo[1];

/* send LSS inquire serial number request */

if (coTfsLssSendInquireSerialNoRequest( pSerialNo ) == 1) {
  /* sent LSS inquire serial number request and received response */
  /* received value can be found in pSerialNo */
}
```
