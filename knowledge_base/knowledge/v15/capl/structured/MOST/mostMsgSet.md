# mostMsgSet

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostMsgSet(mostAmsMessage * msg, long destAdr, char symbolicMessage[], long instId); // form 1
long mostMsgSet(mostAmsMessage * msg, char symbolicMessage[], long instId); // form 2
long mostMsgSet(mostAmsMessage * msg, char symbolicMessage[]); // form 3
```

## Description

Populating an AMS message using the syntax from the MOST specification and the description in the XML function catalog.

PosDescription, TelLen and StreamCases are checked in addition to Funktionsblock, FunktionsID and OpType.

See also Option .MOST: Symbolic Identification of Messages

## Parameters

| Name | Description |
|---|---|
| msg | Message to be populated |
| destAdr | Destination address |
| symbolicMessage | Description of the message content in the following formats: FBlock.InstanceId.Function.OpType(Parameterlist) FBlock.InstanceId.Function.OpType FBlock.Function.OpType(Parameterlist) FBlock.Function.OpType |
| InstId | InstanceID of the function block |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
