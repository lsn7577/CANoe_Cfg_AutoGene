# linSetInterruptingHeaderTransmits

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetInterruptingHeaderTransmits (long enable);
```

## Description

By calling this function, the channel specified by the current bus context will be switched to interrupting mode.

In default mode, requests to transmit headers will be queued until a network idle condition occurs. This means that the networks level has to be recessive for a short period of time. Headers will only start to be transmitted on the network after this condition is met.

Calling linSetInterruptingHeaderTransmits(1) disables the network idle verification. Headers transmitted by CAPL function calls, or by other means in CANoe, will now be transmitted immediately. This will interrupt ongoing transmissions of slave responses if a collision occurs.

This option will affect all headers sent by the LIN hardware.

This function can only be called in CAPL on prestart handlers.

## Parameters

| Name | Description |
|---|---|
| enable | This parameter specifies whether interrupting headers mode on the LIN channel will be enabled or disabled. 0: Disable 1: Enable |

## Return Values

—

## Example

```c
on prestart {
linSetInterruptingHeaderTransmits (1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 | 11.0 | 13.0 | — | — | —✔ |
| Restricted To | LIN | LIN | LIN | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | —✔ |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | ✔ | — | — | —✔ |
