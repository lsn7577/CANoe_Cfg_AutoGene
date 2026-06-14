# J1939ILSetMsgEvent

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILSetMsgEvent( dbMsg msg ); // form 1
long J1939ILSetMsgEvent(dbNode node, dbMsg msg ); // form 2
```

## Description

The message is send immediately, the send type is ignored. The J1939 IL must be in state active and the message must be assigned to the node as Tx message.

To modify signal values prior to message transmission the CAPL functions J1939ILSetSignal or J1939ILSetSignalRaw can be used.

## Parameters

| Name | Description |
|---|---|
| msg | message name from database The message must be a Tx message of the node. |
| node | Simulation node to apply the function |

## Example

```c
on key 't'
{
J1939ILSetMsgEvent( EC1 );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2: form 1 12.0: form 2 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 | J1939 | — | — | form 2 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
