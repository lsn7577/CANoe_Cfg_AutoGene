# coTfsLssSendInquireRevisionNoRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendInquireRevisionNoRequest( dword[] pRevisionNo );
```

## Description

This function sends an Inquire revision number request and waits for the response.

## Return Values

Error code

## Example

```c
dword pRevisionNo[1];

/* send LSS inquire revision number request */

if (coTfsLssSendInquireRevisionNoRequest( pRevisionNo ) == 1) {
  /* sent LSS inquire revision number request and received response */
  /* received value can be found in pRevisionNo */
}
```
