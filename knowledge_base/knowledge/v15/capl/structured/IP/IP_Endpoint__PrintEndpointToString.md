# IP_Endpoint::PrintEndpointToString

> Category: `IP` | Type: `method`

## Syntax

```c
long IP_Endpoint::PrintEndpointToString(char endpoint[]);
```

## Description

Converts the endpoint to a character string with the following form:<TCP/UCP>:<ip_Address>:<Port>

Examples:

## Parameters

| Name | Description |
|---|---|
| endpoint | A character string representing an IP endpoint. |

## Example

```c
void OnReceiveFrom( UdpSocket socket, long result, IP_Endpoint senderEndpoint, byte buffer[], dword size)
{
  char endpointText[60];
  senderEndpoint.PrintEndpointToString(endpointText);
  write("packet from %s received", endpointText );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | 13.0 | — | 4.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | Ethernet | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
