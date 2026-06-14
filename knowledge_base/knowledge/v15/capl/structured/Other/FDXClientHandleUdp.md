# FDXClientHandleUdp

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXClientHandleUdp(dword ipv4Address, dword port); // form 1
long FDXClientHandleUdp(byte ipv6Address[], dword port); // form 2
```

## Description

This function creates an FDX client handle for the FDX client with the specified address.

Prerequisite for the function is to configure UPD/IPv4 or UDP/IPv6 as transport layer for the FDX feature.

## Parameters

| Name | Description |
|---|---|
| ipv4Address | IPv4 address of the FDX clients |
| ipv6Address | IPv6 address of the FDX clients |
| port | UPD port number of the FDX clients. |

## Return Values

If successful, the function returns a value greater than 0, which means the FDX client handle. Values smaller than or equal to zero indicate an error.

## Example

Example for UDP/IPv4

Example for UDP/IPv6

```c
long fdxClientHandle = 0;
dword fdxClientPort = 0;
dword fdxClientAddr = 0;

fdxClientAddr = IpGetAddressAsNumber("127.0.0.1");
fdxClientPort = 2810;
fdxClientHandle = FDXClientHandleUdp(fdxClientAddr, fdxClientPort);
long  fdxClientHandle = 0;
dword fdxClientPort = 0;
byte  fdxClientAddr[16];

IpGetAddressAsArray("::1", fdxClientAddr);
fdxClientPort = 2820;
fdxClientHandle = FDXClientHandleUdp(fdxClientAddr, fdxClientPort);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 SP3: form 1 10.0 SP4: form 2 | 10.0 SP3: form 1 10.0 SP4: form 2 | — | 14 | 2.2 SP2: form 1 2.2 SP3: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
