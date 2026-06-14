# canSetChannelOutput

> Category: `CAN` | Type: `function`

## Syntax

```c
long canSetChannelOutput(long channel, long silent);
```

## Description

Defines the response of the CAN controller to the bus traffic and sets the ACK bit.The CAN transmitter of the channel is switched off. So CANoe does not generate an Ack bit here, and messages can no longer be sent. It is still possible to receive messages.

## Parameters

| Name | Description |
|---|---|
| channel | CAN channel |
| 0 | silent |
| 1 | normal |

## Example

```c
on key 's'
{
   long channel =2;
      long silent =0;
   canSetChannelOutput(channel,silent);
   Write("silent set to %d",silent);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
