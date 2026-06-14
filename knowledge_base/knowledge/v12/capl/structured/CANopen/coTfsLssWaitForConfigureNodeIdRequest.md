# coTfsLssWaitForConfigureNodeIdRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForConfigureNodeIdRequest( byte[] pNID );
```

## Description

The function waits for the configure LSS node id request.

## Return Values

Error code

## Example

```c
dword pNID[1];

/* waits for LSS configure node ID request */
if (coTfsLssWaitForConfigureNodeIdRequest( pNID) == 1) {
  /* received LSS configure node ID request */
  /* received values can be found in pNID[0] */
}
else {
  /* no request received */
  return;
}
```
