# SecurityLocalEncryptAES128CTR

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalEncryptAES128CTR(byte key[], dword keyLength, byte data[], dword dataLength, byte initVector[], dword initVectorLength, byte cipheredData[], dword cipheredDataLength)
```

## Description

Encrypts data with a given key and initialization vector using AES128 (CTR), Padding Mode is not required.

## Parameters

| Name | Description |
|---|---|
| byte key[] | The key to be used for AES (128 bit). |
| dword keyLength | 16 (bytes). |
| byte data[] | The data to encrypt. |
| dword dataLength | The length of the data to encrypt. |
| byte initVector[] | The init vector to be used. |
| dword initVectorLength | 16 (bytes). |
| byte cipheredData [] [Out] | The buffer in which the ciphered data is stored. |
| dword cipheredDataLength [In/Out] | The length of the buffer. Typically this buffer should have the same length as the data to encrypt. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP4 | 11.0 SP4 | — | — | — |
| Restricted To | — | CAN, CAN FD, FR, ETH | CAN, CAN FD, FR, ETH | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
