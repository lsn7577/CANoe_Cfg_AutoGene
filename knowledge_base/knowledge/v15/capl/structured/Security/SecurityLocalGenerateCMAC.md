# SecurityLocalGenerateCMAC

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalGenerateCMAC(byte key[], dword keyLength, byte data[], dword dataLength, byte cmac[], dword cmacLength)
```

## Description

Generates a hash for the given data and key. The generated hash is a CMAC.

## Parameters

| Name | Description |
|---|---|
| byte key[] | The key to be used. |
| dword keyLength | 16 (bytes). |
| byte data[] | The data to encrypt. |
| dword dataLength | The length of the data to encrypt. |
| byte cmac[] [Out] | The generated CMAC. |
| dword cmacLength [In/Out] | The length of the generated CMAC (16 bytes). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3 | 11.0 SP3 | — | — | — |
| Restricted To | — | CAN, CAN FD, FR, ETH | CAN, CAN FD, FR, ETH | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
