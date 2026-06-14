# resetCan

> Category: `CAN` | Type: `function`

## Syntax

```c
void resetCan();
```

## Description

Resets the CAN controller. Can be used to reset the CAN controller after a BUSOFF or to activate configuration changes. Since execution of the function takes some time and the CAN controller is disconnected from the bus briefly, messages can be lost when this is performed.

With this function you can reset CAN1 and CAN2. If only one specific CAN channel is used, resetCan stops with an error and the CAN channels keep offline. In this case the ResetCanEx function has to be used.The function resetCanEx can be used for all channels.

## Return Values

—

## Example

```c
on key 'r' { // Controller is reset after BUSOFF
resetCan();
}
```

## Availability

| Since Version |
|---|
