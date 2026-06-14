# coTfsLssWaitForStoreConfigurationRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForStoreConfigurationRequest( dword errorCode, dword specificError );
```

## Description

This function waits for the LSS store configuration request and sends the response.

## Return Values

Error code

## Example

```c
/* waits for LSS store configuration request */
if (coTfsLssWaitForStoreConfigurationRequest( 0, 0) == 1) {
  /* received LSS store configuration request, sent response with error code and specific error = 0 */
}
```
