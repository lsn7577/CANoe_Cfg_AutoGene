# coTfsLssWaitForInquireSerialNoRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForInquireSerialNoRequest( dword serialNo );
```

## Description

This function waits for the Inquire serial number request and sends the response.

## Return Values

Error code

## Example

```c
/* waits for LSS inquire serial number request */
if (coTfsLssWaitForInquireSerialNoRequest( 0x12345678 ) == 1) {
  /* received LSS inquire serial number request, sent response with serial number */
}
```
