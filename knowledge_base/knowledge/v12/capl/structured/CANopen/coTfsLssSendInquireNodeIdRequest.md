# coTfsLssSendInquireNodeIdRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendInquireNodeIdRequest( dword[] pNodeId );
```

## Description

This function sends an Inquire node-ID request and waits for the response.

## Return Values

Error code

## Example

```c
byte pNodeId[1];

/* send LSS inquire node ID request */

if (coTfsLssSendInquireNodeIdRequest( pNodeId ) == 1) {
  /* sent LSS inquire node ID request and received response */
  /* received value can be found in pNodeId */
}
```
