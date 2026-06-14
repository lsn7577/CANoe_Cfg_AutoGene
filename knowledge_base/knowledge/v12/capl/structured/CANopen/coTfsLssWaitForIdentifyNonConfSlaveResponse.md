# coTfsLssWaitForIdentifyNonConfSlaveResponse

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForIdentifyNonConfSlaveResponse( void );
```

## Description

This function waits for an Identify non-configured slave response.

## Return Values

Error code

## Example

```c
/* wait for identify non configured slave response */
if (coTfsLssWaitForIdentifyNonConfSlaveResponse() == 1) {
  /* response received */
}
```
