# DoIP_UDPSend

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_UDPSend(dword payloadType, byte payload[], dword payloadLen);
long DoIP_UDPSend(char IPaddress[], dword payloadType, byte payload[], dword payloadLen);
```

## Description

Sends a DoIP PDU with valid layout to peer(s) as UDP frame. The configured DoIP version is used.

## Parameters

| Name | Description |
|---|---|
| IPaddress | If given, do not send to the selected peer, but to this address. |
| payloadType | Type to send, i.e. this can be any value. [0; 0xFFFF] |
| payload | The data following the generic DoIP header. |
| payloadLen | Payload length. |

## Return Values

Error code

## Example

```c
// Send a DoIP PDU with valid layout but non-standard type
// to a specific vehicle
BYTE payload[3] = { 0x12, 0x34, 0x45};
DoIP_UDPSend( "169.254.123.45", 0xF333, payload, elcount( payload));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 SP4 | — | — | — | 1.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
