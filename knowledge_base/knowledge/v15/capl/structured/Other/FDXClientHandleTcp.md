# FDXClientHandleTcp

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXClientHandleTcp(dword ipv4Address, dword port); // form 1
long FDXClientHandleTcp(byte ipv6Address[], dword port); // form 2
```

## Description

This function creates an FDX client handle for the FDX client with the specified address.

Prerequisite for the function is to configure TCP/IPv4 or TCP/IPv6 as transport layer for the FDX feature.

## Parameters

| Name | Description |
|---|---|
| ipv4Address | IPv4 address of the FDX clients |
| ipv6Address | IPv6 address of the FDX clients |
| port | TCP port number of the FDX clients. |

## Return Values

If successful, the function returns a value greater than 0, which means the FDX client handle. Values smaller than or equal to zero indicate an error.

## Example

Example for TCP/IPv4

Example for TCP/IPv6

```c
long fdxClientHandle = 0;
dword fdxClientPort = 0;
dword fdxClientAddr = 0;

fdxClientAddr = IpGetAddressAsNumber("127.0.0.1");
fdxClientPort = 2810;
fdxClientHandle = FDXClientHandleTcp(fdxClientAddr, fdxClientPort);
long  fdxClientHandle = 0;
dword fdxClientPort = 0;
byte  fdxClientAddr[16];

IpGetAddressAsArray("::1", fdxClientAddr);
fdxClientPort = 2820;
fdxClientHandle = FDXClientHandleTcp(fdxClientAddr, fdxClientPort);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP4 | 13.0 | — | 14 | 2.2 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
