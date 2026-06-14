# LINtp_DataInd

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_DataInd(long count); // form 1
void LINtp_DataInd(long count, dword NAD); // form 2
```

## Description

Callback indicates the reception of data. In a Slave node the NAD indicates the address of the destination node or 0x7E if data was sent to a functional group, in a Master the address of the sending slave.

Use LINtp_GetRxData to retrieve the data.

## Parameters

| Name | Description |
|---|---|
| count | Number of bytes received. |
| NAD | Node address of the slave node that is the sender (if called in the master node) or receiver of the data (if called in a slave node). |

## Return Values

—

## Example

```c
// Before CANoe 8.5, use this signature:
// LINtp_DataInd(long count) { ... }

// Only in CANoe 8.5 or later
LINtp_DataInd(long count, DWORD nad)
{
  byte rxBuffer[4096];
  LINtp_GetRxData(rxBuffer, count);

  if( nad == 0x7E)
    write( "received functional request of %d byte", count);
  else
  write( "received %d bytes from/for node %02x", count, nad);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | All: form 1 8.5: form 2 | — | — | — | — |
| Restricted To | — | LIN Real bus mode | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
