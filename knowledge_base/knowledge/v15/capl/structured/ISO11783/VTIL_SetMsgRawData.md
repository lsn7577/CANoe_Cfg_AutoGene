# VTIL_SetMsgRawData

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SetMsgRawData( dbMsg msg, long dataSize, byte data[] ); // form 1
long VTIL_SetMsgRawData( dbNode vt, dbMsg msg, long dataSize, char data[] ); // form 2
```

## Description

Sets the data bytes of the message. The length of the parameter group is adjusted to size of parameter dataSize.

## Parameters

| Name | Description |
|---|---|
| msg | message name from database, must be assigned to the node as Tx message |
| dataSize | number of data bytes |
| data | data bytes |
| pgData | data and DLC are taken from this parameter group |
| vt | VT simulation node to apply the function |

## Example

Example form 1

```c
void SendPointingEvent(word x, word y, byte touchState)
{
  char buf[8];
  buf[0] = 0x02; // Pointing Event
  buf[1] = x & 0xFF;
  buf[2] = (x >> 8) & 0xFF;
  buf[3] = y & 0xFF;
  buf[4] = (y >> 8) & 0xFF;
  buf[5] = touchState;
  buf[6] = 0xFF;
  buf[7] = 0xFF;
  VTIL_SetMsgRawData(VT12_VT, elCount(buf), buf);
  VTIL_SetMsgEvent(VT12_VT);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
