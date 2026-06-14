# SecurityLocalDecryptAES256CBC

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalDecryptAES256CBC(byte key[], dword keyLength, byte cipheredData[], dword cipheredDataLength, byte initVector[], dword initVectorLength, byte plainData[], dword plainDataLength)
```

## Description

Decrypts ciphered data with a given key and initialization vector using AES256 (CBC), Padding Mode PKCS5.

## Parameters

| Name | Description |
|---|---|
| byte key[] | The key to be used for AES (256 bit). |
| dword keyLength | 32 (bytes). |
| byte cipheredData[] | The ciphered data to decrypt. |
| dword cipheredDataLength | The length of the ciphered data. |
| byte initVector[] | The init vector to be used. |
| dword initVectorLength | 16 (bytes). |
| byte plainData[] [Out] | The buffer in which the plain data is stored. |
| dword plainDataLength [In/Out] | The length of the buffer for the plain data. Typically this buffer should have the same length as the ciphered data buffer. |

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
