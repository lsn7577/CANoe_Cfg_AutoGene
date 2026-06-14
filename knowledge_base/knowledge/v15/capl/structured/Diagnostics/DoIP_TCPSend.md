# DoIP_TCPSend

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_TCPSend(dword payloadType, byte payload[], dword payloadLen);
long DoIP_TCPSend(dword protocolID, dword payloadType, byte payload[], dword payloadLen);
```

## Description

Sends a DoIP PDU with valid layout on the open TCP connection.

## Parameters

| Name | Description |
|---|---|
| protocolD | If given, this will replace the configured protocol version in the DoIP PDU.[0; 255] |
| payloadType | Type to send, i.e. this can be any value.[0; 0xFFFF] |
| payload | The data following the generic DoIP header. |
| payloadLen | Length of the data following the header. |

## Return Values

Error code, e.g. connection not established yet.

## Example

```c
// When a vehicle is connected, send a non-standard frame to the peer
On key '1'
{
  BYTE payload[3] = { 0x11, 0x22, 0x33 };
  // the frame type 0xF222 is manufacturer-specific
  DoIP_TCPSend( 0xF222, payload, elcount( payload));
}
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
