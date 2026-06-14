# coTfsLssSendIdentifySlaveResponse

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendIdentifySlaveResponse( void );
```

## Description

This function sends an Identify slave protocol response message.

## Return Values

Error code

## Example

```c
/* sends LSS identify slave protocol response message */

if (coTfsLssSendIdentifySlaveResponse() == 1) {
  /* message sent */
}
```
