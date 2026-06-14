# mostPrepareReport

> Category: `MOST` | Type: `function`

## Syntax

```c
mostPrepareReport(mostAmsMessage * msgCommand, mostAmsMessage * msgReport);
```

## Description

Preparation of an AMS message as response (OpType>=9) to a received command message (OpType<9).

The destination address of the report message is set to the source address of the command message. The parameters FBlockId, InstId and FunctionId in msgReport are set as given by the msgCommand. Any wildcard InstId in msgCommand is transferred to a concrete value in msgReport with the help of the device’s Local FBlock list.

According to the MOST specification, the OpTypes are converted by the command into the associated report OpType:

Messages with Ack-OpTypes contain a sender handle in the first two data bytes. This sender handle is also set in the first two data bytes of the report message.

## Parameters

| Name | Description |
|---|---|
| msgCommand | Command message to be answered. |
| msgReport | Message that should serve as a response. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
