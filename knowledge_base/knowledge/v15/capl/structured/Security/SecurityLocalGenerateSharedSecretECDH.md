# SecurityLocalGenerateSharedSecretECDH

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalGenerateSharedSecretECDH(byte publicKey[], dword publicKeyLength, byte privateKey[], dword privateKeyLength, byte sharedSecret[], dword* sharedSecretLength)
```

## Description

Generates a shared Secret between A and B for a given public key of A and private Key of B. The Elliptic Curve Diffie-Hellman (ECDH) protocol (X25519) is used.

## Parameters

| Name | Description |
|---|---|
| byte publicKey [] | The public key of A. |
| dword publicKeyLength | 32 bytes. |
| byte privateKey[] | The private key of B. |
| dword privateKeyLength | 32 bytes. |
| byte sharedSecret[] [Out] | The generated shared secret. |
| dword sharedSecretLength [In/Out] | The length of the generated shared secret (32 bytes). |

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
