# coTfsLssWaitForIdentifySlaveResponse

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForIdentifySlaveResponse( void );
```

## Description

This function waits for the Identify slave protocol response message.

## Return Values

Error code

## Example

```c
/* waits for identify slave protocol response message */
if (coTfsLssWaitForIdentifySlaveResponse() == 1) {
  /* waits for LSS identify slave protocol response message */
}
```
