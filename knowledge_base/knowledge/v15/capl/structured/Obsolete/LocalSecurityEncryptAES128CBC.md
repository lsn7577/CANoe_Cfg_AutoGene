# LocalSecurityEncryptAES128CBC

> Category: `Obsolete` | Type: `notes`

## Description

Replaced by SecurityLocalEncryptAES128CBC.

| Deprecated Function Replaced by SecurityLocalEncryptAES128CBC. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long LocalSecurityEncryptAES128CBC(BYTE[] key, dword keyLength, BYTE[] data, dword dataLength, BYTE[] initVector, dword initVectorLength, BYTE[] cipheredData, dword cipheredDataLength) |  |  |  |
| Function | Encrypts data with a given key and initialization vector. The encryption is AES128 (CBC), PKCS5 Padding. |  |  |  |
| Parameters | key The key to be used for AES (128 bit) |  |  |  |
| keyLength 16 (bytes) |  |  |  |  |
| plainData The data to encrypt |  |  |  |  |
| plainDataLength The length of the data |  |  |  |  |
| initVector The init vector to be used |  |  |  |  |
| initVectorLength 16 (bytes) |  |  |  |  |
| cipheredData The buffer in which the ciphered data is stored. |  |  |  |  |
| cipheredDataLength The length of the buffer.Typically this buffer has to be 16 bytes longer than the length of the data to encrypt. |  |  |  |  |
| Return Values | Successful = 1, Failed <= 0 |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 11.0 SP3 | - | — | • |  |

| Version 15© Vector Informatik GmbH |
|---|
