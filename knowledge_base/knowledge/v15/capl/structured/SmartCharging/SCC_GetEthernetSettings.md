# SCC_GetEthernetSettings

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_GetEthernetSettings(byte MacAddress[], byte IPv4Address[], dword& IPv4Available, byte IPv6Address[], dword& IPv6Available, dword& UDPPort, dword& TCPPort)
```

## Description

Retrieves the configured addresses and ports for the SCC node. These values may originate from the CANoe configuration or from the DLL’s XML configuration.

## Parameters

| Name | Description |
|---|---|
| MacAddress | 6 byte MAC address. |
| IPv4Address | 4 byte IPv4 address. |
| IPv4Available | 1 if IPv4Address is valid, else 0. |
| IPv6Address | 16 byte IPv6 address. |
| IPv6Available | 1 if IPv6Address is valid, else 0. |
| UDPPort | UDP port number for SECC Discovery. |
| TCPPort | TCP port number for Vehicle2Grid TP. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | — | — | — | 3.0 SP3 |
| Restricted To | — | Ethernet .SmartCharging | — | — | — | Ethernet .SmartCharging |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
