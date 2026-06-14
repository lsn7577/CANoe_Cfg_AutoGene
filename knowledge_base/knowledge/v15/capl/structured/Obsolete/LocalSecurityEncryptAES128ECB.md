# LocalSecurityEncryptAES128ECB

> Category: `Obsolete` | Type: `notes`

## Description

Replaced by SecurityLocalEncryptAES128ECB.

The key to be used for AES (128 bit)

16 (bytes)

The data to encrypt

The length of the data

The buffer in which the ciphered data is stored.

The length of the buffer. Typically this buffer has to be 16 bytes longer than the length of the data to encrypt.

| Deprecated Function Replaced by SecurityLocalEncryptAES128ECB. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long LocalSecurityEncryptAES128ECB(BYTE[] key, dword keyLength, BYTE[] data, dword dataLength, BYTE[] cipheredData, dword cipheredDataLength) |  |  |  |
| Function | Encrypts data with a given key and initialization vector. The encryption is AES128 (ECB), PKCS5 Padding. ECB Mode does not use an initialization vector. |  |  |  |
| Parameters | key The key to be used for AES (128 bit) |  |  |  |
| keyLength 16 (bytes) |  |  |  |  |
| plainData The data to encrypt |  |  |  |  |
| plainDataLength The length of the data |  |  |  |  |
| cipheredData The buffer in which the ciphered data is stored. |  |  |  |  |
| cipheredDataLength The length of the buffer. Typically this buffer has to be 16 bytes longer than the length of the data to encrypt. |  |  |  |  |
| Return Values | Successful = 1, Failed <= 0 |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 11.0 SP2 | — | — | • |  |

| Version 15© Vector Informatik GmbH |
|---|
