# GBT27930IL_SetMsgRawData

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_SetMsgRawData(dbMsg msg, long dataSize, byte data[] ); // form 1
long GBT27930IL_SetMsgRawData(dbNode node, dbMsg msg, long dataSize, byte data[] ); // form 2
long GBT27930IL_SetMsgRawData(dbMsg msg, long dataSize, char data[] ); // form 3
long GBT27930IL_SetMsgRawData(dbNode node, dbMsg msg, long dataSize, char data[] ); // form 4
long GBT27930IL_SetMsgRawData(dbMsg msg, pg * pgData ); // form 5
long GBT27930IL_SetMsgRawData(dbNode node, dbMsg msg, pg * pgData ); // form 6
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
| node | Simulation node to apply the function |

## Example

```c
on key 't'
{
  char data[10] = "TPMS*V1.0*";
GBT27930IL_SetMsgRawData( ECUID, elCount(data), data );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 and Smart Charging | J1939 and Smart Charging | — | — | form 2, 4, 6 J1939 and Smart Charging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3, 5) | ✔ (form 1, 3, 5) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4, 6) | ✔ (form 2, 4, 6) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4, 6) | ✔ (form 2, 4, 6) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
