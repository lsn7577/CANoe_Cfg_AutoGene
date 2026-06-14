# FSIL_SetMsgEvent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_SetMsgEvent( dbMsg msg ); // form 1
long FSIL_SetMsgEvent( dbNode fs, dbMsg msg ); // form 2
```

## Description

The message is send immediately, the send type is ignored. The FS IL must be in state active and the message must be assigned to the node as Tx message.

To modify signal values prior to message transmission the CAPL functions FSIL_SetSignal or FSIL_SetSignalRaw can be used.

## Parameters

| Name | Description |
|---|---|
| msg | Message name from database. The message must be a Tx message of the node. |
| fs | FS simulation node to apply the function |

## Example

```c
on key 'i'
{
FSIL_SetMsgEvent( ICC_FS );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
