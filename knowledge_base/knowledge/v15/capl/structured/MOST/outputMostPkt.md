# outputMostPkt

> Category: `MOST` | Type: `function`

## Syntax

```c
outputMostPkt(long channel, long destadr, long pktdatalen, BYTE pktdata[]);
```

## Description

Sends out packets over the asynchronous MOST channel.

## Parameters

| Name | Description |
|---|---|
| channel | Channel number |
| destadr | Destination address |
| pktdatalen | Number of bytes to be sent. MOST25/MOST50: 0 < pktdatalen = 1014MOST150: 0 < pktdatalen = 1524 |
| pktdata[] | Useful data |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 After measurement start | MOST25 MOST50 MOST150 After measurement start | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
