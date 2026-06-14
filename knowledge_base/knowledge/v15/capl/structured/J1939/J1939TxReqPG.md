# J1939TxReqPG

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939TxReqPG( dword ecuHandle, dword pgn, dword destination, dword priority, dword dlc, char data[] );
dword J1939TxReqPG( dword ecuHandle, dword pgn, dword destination, dword priority, dword dlc, byte data[] );
```

## Description

Sends any PG. The node layer handles fragmenting automatically. As soon as the PG has been transferred, J1939TxIndication() is called. This gives the application the possibility of protocol monitoring, especially in the case of fragmented PGs.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| pgn | PGN which should be sent |
| destination | destination address or global address (255) |
| priority | priority |
| dlc | number of data bytes |
| data | data |

## Return Values

0 on success or error code

## Example

```c
char data[14];

// global parameter group
res = J1939TxReqPG(ecuHdl, 
 0xFE45, 0xFF, 4, 14, data);

// specific 
 parameter group:
res = J1939TxReqPG(ecuHdl, 0xE600, 0x09, 4, 
 14, data);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
