# Iso11783TxReqPG

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783TxReqPG( dword ecuHandle, dword pgn, dword destination, dword priority, dword dlc, char data[] );
dword Iso11783TxReqPG( dword ecuHandle, dword pgn, dword destination, dword priority, dword dlc, byte data[] );
```

## Description

Sends any PG. The node layer handles fragmenting automatically. As soon as the PG has been transferred, Iso11783AppTxIndication() is called. This gives the application the possibility of protocol monitoring, especially in the case of fragmented PGs.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| pgn | PGN which should be sent |
| destination | Destination address or global address (255) |
| priority | Priority |
| dlc | Number of data bytes |
| data | Data |

## Return Values

0 on success or error code

## Example

```c
char data[14];

// global parameter group
res = Iso11783TxReqPG(ecuHdl, 
 0xFE45, 0xFF, 4, 14, data);

// specific 
 parameter group:
res = Iso11783TxReqPG(ecuHdl, 0xE600, 0x09, 4, 
 14, data);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | Iso11783 | Iso11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
