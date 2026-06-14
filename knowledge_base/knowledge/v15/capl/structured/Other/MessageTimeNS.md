# MessageTimeNS

> Category: `Other` | Type: `function`

## Syntax

```c
float MessageTimeNS(message msg); // from 1
float MessageTimeNS(linFrame msg); // from 2
float MessageTimeNS(mostMessage msg); // from 3
float MessageTimeNS(mostAmsMessage msg); // from 4
float MessageTimeNS(mostRawMessage msg); // from 5
```

## Description

Returns the time stamp in nanoseconds.

The time stamp that can be polled with this function has a greater precision than the msg.TIME time stamp, whereby the precision depends on the CAN or LIN hardware that is being used.

## Parameters

| Name | Description |
|---|---|
| message | CAN message |
| linFrame | LIN frame |
| mostMessage, mostAmsMessage, mostRawMessage | MOST message |

## Return Values

Time stamp of the message in ns.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1 | 5.1 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
