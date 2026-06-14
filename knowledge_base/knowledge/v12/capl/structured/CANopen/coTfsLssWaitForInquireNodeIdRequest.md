# coTfsLssWaitForInquireNodeIdRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForInquireNodeIdRequest( dword nodeId );
```

## Description

This function waits for the Inquire node-ID request and sends the response.

## Return Values

Error code

## Example

```c
/* waits for LSS inquire node ID request */
if (coTfsLssWaitForInquireNodeIdRequest( 112 ) == 1) {
  /* received LSS inquire node ID request, sent response with node ID */
}
```
