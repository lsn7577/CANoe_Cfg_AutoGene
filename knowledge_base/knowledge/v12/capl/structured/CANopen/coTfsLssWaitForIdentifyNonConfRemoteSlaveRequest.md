# coTfsLssWaitForIdentifyNonConfRemoteSlaveRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForIdentifyNonConfRemoteSlaveRequest( void );
```

## Description

This function waits for an Identify non-configured remote slave response.

## Return Values

Error code

## Example

```c
/* waits for a LSS identify non configured remote slave request */
if (coTfsLssWaitForIdentifyNonConfRemoteSlaveRequest() == 1) {
  /* request received */
}
```
