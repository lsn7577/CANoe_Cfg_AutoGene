# _DoIP_UDPInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long _DoIP_UDPInd( char IPaddress[], WORD port, BYTE data[]);
```

## Description

An UDP packet was received. All packets are forwarded to this callback function, and it can decide whether processing of the packet stops, or is continued.

The sender IP address and source port is given as first arguments.

## Parameters

| Name | Description |
|---|---|
| IPaddress | Address in text form, e.g. “169.254.32.1” (IPv4) or “2001::1” (IPv6). |
| port | IP source port of the packet at the sender. |
| data | The raw data received, including complete header, if present. |

## Example

```c
// If packet with payload type 0xF000 is received, answer with a 0xF001 packet
// and stop processing. Otherwise process the packet normally.
long _DoIP_UDPInd( char IPaddress[], WORD port, BYTE data[])
{
  WORD payloadType;
  BYTE response[2] = { 0x12, 0x34 };
  if( elcount(data) < 8)
    return 0;
  payloadType = (data[2] << 8) + data[3];
  if( payloadType != 0xF000)
    return 0;

  DoIP_UDPSendPort( IPaddress, port, 0xF001, response, elcount( response));
  return -1; // we process this frame
}
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
