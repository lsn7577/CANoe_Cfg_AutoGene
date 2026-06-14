# LocalSecurityGenerateCMAC

> Category: `Obsolete` | Type: `notes`

## Description

Replaced by SecurityLocalGenerateCMAC.

| Deprecated Function Replaced by SecurityLocalGenerateCMAC. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long LocalSecurityGenerateCMAC(BYTE[] key, dword keyLength, BYTE[] data, dword dataLength, BYTE[] output, dword outputLength) |  |  |  |
| Function | Generates a hash for the given data and key. The generated Hash is a CMAC. |  |  |  |
| Parameters | key The key to be used. |  |  |  |
| keyLength 16 (bytes) |  |  |  |  |
| data The data to encrypt. |  |  |  |  |
| dataLength The length of the data. |  |  |  |  |
| output The generated cmac. |  |  |  |  |
| outputLength 16 bytes |  |  |  |  |
| Return Values | Successful = 1, Failed <= 0 |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 11.0 SP2 | — | — | • |  |

| Version 15© Vector Informatik GmbH |
|---|
