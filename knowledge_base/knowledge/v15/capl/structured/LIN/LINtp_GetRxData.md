# LINtp_GetRxData

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_GetRxData(byte data[], long size);
```

## Description

Retrieve data bytes received.

## Parameters

| Name | Description |
|---|---|
| data | Copy bytes into this buffer. |
| size | Maximum number of bytes to copy. |

## Return Values

—

## Example

```c
LINtp_DataInd(long count, DWORD nad)
{
  byte rxBuffer[4096];
  LINtp_GetRxData(rxBuffer, count);
  write( "received <%02x ...> from/for node %02x"
  , rxBuffer[0], nad);
}
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
