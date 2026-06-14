# coTfsLssWaitForInquireVendorIdRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForInquireVendorIdRequest( dword vendorId );
```

## Description

This function waits for the Inquire vendor-ID request and sends the response.

## Return Values

Error code

## Example

```c
/* waits for LSS inquire vendor ID request */
if (coTfsLssWaitForInquireVendorIdRequest( 0x12345678) == 1) {
  /* received LSS inquire vendor ID request, sent response with vendorId */
}
```
