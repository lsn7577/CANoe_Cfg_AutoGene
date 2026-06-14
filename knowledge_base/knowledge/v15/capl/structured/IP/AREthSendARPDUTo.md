# AREthSendARPDUTo

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthSendARPDUTo( dword aep, dword dstIPv4Addr, dword dstPort, dword bufferLength, char buffer[], dword headerID ); // form 1
long AREthSendARPDUTo( dword aep, dword dstIPv4Addr, dword dstPort, dword bufferLength, byte buffer[], dword headerID ); // form 2
long AREthSendARPDUTo( dword aep, dword dstIPv4Addr, dword dstPort, dword bufferLength, struct buffer, dword headerID ); // form 3
long AREthSendARPDUTo( dword aep, byte dstIPv6Addr[], dword dstPort, dword bufferLength, char buffer[], dword headerID ); // form 4
long AREthSendARPDUTo( dword aep, byte dstIPv6Addr[], dword dstPort, dword bufferLength, byte buffer[], dword headerID ); // form 5
long AREthSendARPDUTo( dword aep, byte dstIPv6Addr[], dword dstPort, dword bufferLength, struct buffer, dword headerID ); // form 6
long AREthSendARPDUTo( dword aep, IP_Endpoint dstIPEndpoint, dword bufferLength, char buffer[], dword headerID ); // form 7
long AREthSendARPDUTo( dword aep, IP_Endpoint dstIPEndpoint, dword bufferLength, byte buffer[], dword headerID ); // form 8
long AREthSendARPDUTo( dword aep, IP_Endpoint dstIPEndpoint, dword bufferLength, struct buffer, dword headerID ); // form 9
```

## Description

Transmits data as AUTOSAR PDU via an Ethernet connection with activated Header option. Before transmitting each AUTOSAR PDU gets an Header that contains an ID and length.

## Parameters

| Name | Description |
|---|---|
| aep | Handle of an application endpoint that was opened with AREthOpenLocalApplicationEndpoint. |
| dstIPv4Addr | IPv4 address of the target as dword, e.g. converted with ipGetAddressAsNumber. |
| dstIPv6Addr | IPv6 address of the target as byte array, e.g. converted with ipGetAddressAsArray. |
| dstPort | UDP or TCP port of the target. |
| dstIPEndpoint | Object of type IP_Endpoint that contains the address/port of the target. |
| bufferLength | Buffer length of the data. The length is written in the preceded header during transmission. |
| buffer | Data to transmit without header. |
| headerId | ID which is to be written in the header. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2: form 1-3 10.0 SP4: form 4-6 12.0 SP2: form 7-9 | — | — | — | 2.1 SP3: form 1-3 2.2 SP4: form 4-6 4.0 SP2: form 7-9 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
