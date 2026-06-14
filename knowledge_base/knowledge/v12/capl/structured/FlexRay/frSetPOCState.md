# frSetPOCState

> Category: `FlexRay` | Type: `function`

## Syntax

```c
long frSetPOCState( long channel, long ccNumber, long pocState )
```

## Description

This function puts the FlexRay Communication Controller (CC) into the desired Protocol Operation Mode (POC state). The function is non-blocking. That means, the function will return before the CC has reached the desired POC-state.

All E-Ray POC-state changes can be monitored with the status- or POC-state-events. A status event is generated as soon as the second CC has reached the desired POC-state.

The diagram shows the several states and the corresponding transitions in the protocol operation control process:

## Return Values

0: Error (wrong parameter, or the POC state can not be reached)

## Availability

| Since Version |
|---|
