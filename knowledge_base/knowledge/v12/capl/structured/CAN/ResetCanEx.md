# ResetCanEx

> Category: `CAN` | Type: `function`

## Syntax

```c
void ResetCanEx(long channel);
```

## Description

Resets the CAN controller for one specific CAN channel. Can be used to reset the CAN controller after a BUSOFF or to activate configuration changes. Since execution of the function takes a certain amount of time and the CAN controller is disconnected from the bus for a brief period messages may be lost.

## Return Values

—

## Example

```c
on key 'r' { // After BUSOFF the controller on Channel 2 is reset
resetCanEx(2);
}
```

## Availability

| Since Version |
|---|
