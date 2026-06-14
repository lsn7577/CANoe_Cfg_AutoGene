# Iso11783IL_SetMsgEvent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_SetMsgEvent( dbMsg msg );
```

## Description

The message is send immediately, the send type is ignored. The ISO11783 IL must be in state active and the message must be assigned to the node as Tx message.

To modify signal values prior to message transmission the CAPL functions Iso11783IL_SetSignal or Iso11783IL_SetSignalRaw can be used.

## Parameters

| Name | Description |
|---|---|
| msg | message name from database The message must be a Tx message of the node. |

## Example

```c
on key 't'
{
Iso11783IL_SetMsgEvent( EC1 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
