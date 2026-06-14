# linSetInterruptingHeaderTransmits

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetInterruptingHeaderTransmits (long enable)
```

## Description

By calling this function, the channel specified by the current bus context will be switched to interrupting mode.

In default mode, requests to transmit headers will be queued until a network idle condition occurs. This means that the networks level has to be recessive for a short period of time. Headers will only start to be transmitted on the network after this condition is met.

Calling linSetInterruptingHeaderTransmits(1) disables the network idle verification. Headers transmitted by CAPL function calls, or by other means in CANoe, will now be transmitted immediately. This will interrupt ongoing transmissions of slave responses if a collision occurs.

This option will affect all headers sent by the LIN hardware.

This function can only be called in CAPL on prestart handlers.

## Return Values

—

## Example

```c
on prestart {
linSetInterruptingHeaderTransmits (1);
}
```

## Availability

| Since Version |
|---|
