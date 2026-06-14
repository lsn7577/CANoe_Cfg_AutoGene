# OnIpGetHostByName

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnIpGetHostByName(long result, char hostname[], dword ipv4Address[], dword count); // from 1
void OnIpGetHostByName(long result, char hostname[], byte ipv6Address[][], dword count); // from 2
```

## Description

The callback is called if a previous call of IpGetHostByName is returned with error code WSAEWOULDBLOCK (10035) and the dissolve of the address is completed.

## Parameters

| Name | Description |
|---|---|
| result | The result of the function. See the Winsock 2 Error Codes for possible errors. Typical values are: result: 0: The function completed successfully. WSAHOST_NOT_FOUND (11001): Host not found. |
| hostname | The hostname which was resolved by the function. |
| ipv4Address | Array in which the determined IPv4 addresses are written. |
| ipv6Address | Array in which the determined IPv6 addresses are written. |
| count | Number of determined addresses. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 SP4 | 8.5 SP4 | 13.0 | — | — | 2.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
