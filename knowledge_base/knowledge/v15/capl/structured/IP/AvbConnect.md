# AvbConnect

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbConnect(dword talkerHandle, byte remoteMacAddress[], char onConnectCallback[]); // form 1
dword AvbConnect(dword talkerHandle, dword remoteIpV4Address, dword port, char onConnectCallback []); // form 2
dword AvbConnect(dword talkerHandle, byte remoteIpV6Address[], dword port, char onConnectCallback []); // form 3
dword AvbConnect(dword talkerHandle, onConnectCallback []); // form 4
```

## Description

The function establishes a connection with the specified location. If the connect operation does not complete immediately the operation is performed asynchronously and the function will return 460609. In this case the passed CAPL callback OnAvbConnect will be called on completion (successful or not).

Used transport protocols:

## Parameters

| Name | Description |
|---|---|
| talkerHandle | The Talker handle. |
| remoteMacAddress | The (6 byte) destination MAC address (usually a multicast address). |
| remoteIpV4Address | The (4 byte) destination IPv4 address (usually a multicast address). |
| remoteIpV6Address | The (16 byte) destination IPv6 address (usually a multicast address). |
| onConnectCallback | The name of the CAPL callback function (see OnAvbConnect). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP2: form 1 10.0: form 3 10.0 SP3: form 2, 4 | — | — | — | 2.0 SP2: form 1 2.2: form 3 2.2 SP2: form 2, 4 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
