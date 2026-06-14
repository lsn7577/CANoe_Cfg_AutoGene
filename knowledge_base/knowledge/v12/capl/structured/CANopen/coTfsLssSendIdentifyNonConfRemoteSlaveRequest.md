# coTfsLssSendIdentifyNonConfRemoteSlaveRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
coTfsLssSendIdentifyNonConfRemoteSlaveRequest() == 1);
```

## Description

This function sends an Identify non-configured remote slave response.

## Return Values

Error code

## Example

```c
/* send LSS identify non configured remote slave request */

if (coTfsLssSendIdentifyNonConfRemoteSlaveRequest() == 1) {
  /* request sent */
}
```
