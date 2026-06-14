# coTfsLssSendIdentifyNonConfSlaveResponse

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendIdentifyNonConfSlaveResponse( void );
```

## Description

This function sends an Identify non-configured remote slave response.

## Return Values

Error code

## Example

```c
/* sends LSS identify non configured slave protocol response message */

if (coTfsLssSendIdentifyNonConfSlaveResponse() == 1) {
/* message sent */
}
```
