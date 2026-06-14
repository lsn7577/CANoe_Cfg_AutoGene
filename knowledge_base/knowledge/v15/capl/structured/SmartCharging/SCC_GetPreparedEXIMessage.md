# SCC_GetPreparedEXIMessage

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_GetPreparedEXIMessage ( byte data[], dword& dataLength ) // form 1
long SCC_GetPreparedEXIMessage ( byte data[], dword& dataLength, dword ConfigSection ) // form 2
```

## Description

Finalizes a message without sending. The message data is returned to an output buffer instead. Usually this data consists of the V2G header and the EXI encoded V2G payload.

## Parameters

| Name | Description |
|---|---|
| Data | Output buffer for the message. Make sure to use a buffer that is large enough (some messages may take up to 10 kB). |
| DataLength | Length of the copied data. |
| ConfigSection | ID of the config section where the certificates can be found. |

## Return Values

The Id attribute of the message body, if existing (to the output buffer).

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3: form 1, 2 | — | — | — | 3.0 SP3: form 1, 2 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
