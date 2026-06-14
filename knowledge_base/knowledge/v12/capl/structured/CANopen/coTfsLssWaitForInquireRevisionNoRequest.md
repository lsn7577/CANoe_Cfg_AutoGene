# coTfsLssWaitForInquireRevisionNoRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForInquireRevisionNoRequest( dword revisionNo );
```

## Description

This function waits for the Inquire revision number request and sends the response.

## Return Values

Error code

## Example

```c
/* waits for LSS inquire revision number request */
if (coTfsLssWaitForInquireRevisionNoRequest( 0x12345678 ) == 1) {
  /* received LSS inquire revision number request, sent response with revision number */
}
```
