# DoIP_UDPSendPort

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
ong DoIP_UDPSendPort(char IPaddress[], dword port, dword payloadType, byte payload[], dword payloadLen);
```

## Description

Sends a DoIP PDU with valid layout to peer(s) as UDP frame. The configured DoIP version is used.

## Parameters

| Name | Description |
|---|---|
| IPaddress | Send to this address, may be a broadcast address. |
| port | Destination port for the UDP packet. |
| payloadType | Type to send, i.e. this can be any value. [0; 0xFFFF] |
| payload | The data following the generic DoIP header. |
| payloadLen | Payload length. |

## Return Values

Error code

## Example

```c
// Send an invalid identification request to a non-standard port of a 
// specific vehicle that must ignore it
BYTE rawData[8] = { 0x02,0xFF /*wrong!*/, 0x00,0x01, 0x00,0x00,0x00,0x00};
DoIP_UDPSendPort( "169.254.123.45", 13401 /* non standard */, rawData, elcount( rawData));
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | — | — | — | 2.1 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
