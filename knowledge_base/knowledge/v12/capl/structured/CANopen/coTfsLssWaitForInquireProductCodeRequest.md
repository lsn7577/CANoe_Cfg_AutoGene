# coTfsLssWaitForInquireProductCodeRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForInquireProductCodeRequest( dword productCode );
```

## Description

This function waits for the Inquire product code request and sends the response.

## Return Values

Error code

## Example

```c
/* waits for LSS inquire product code request */
if (coTfsLssWaitForInquireProductCodeRequest( 0x12345678) == 1) {
  /* received LSS inquire vendor ID request, sent response with product code */
}
```
