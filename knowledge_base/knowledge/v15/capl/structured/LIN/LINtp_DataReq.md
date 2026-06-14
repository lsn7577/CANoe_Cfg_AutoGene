# LINtp_DataReq

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_DataReq(byte data[], long numData, long NAD);
```

## Description

Send the given data. Once all data has been sent, the callback LINtp_DataCon is called. If there has been an error, LINtp_ErrorInd is called.

## Parameters

| Name | Description |
|---|---|
| data | Data to send. |
| numData | Number of bytes to send. |
| NAD | Slave node address |

## Return Values

—

## Example

```c
BYTE data[20];
LINtp_DataReq( data, elcount(data), 0x12);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | All | — | — | — | — |
| Restricted To | — | LIN Real bus mode | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
