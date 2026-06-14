# LocalSecurityEncryptAES128CBC

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long LocalSecurityEncryptAES128CBC(BYTE[] key, dword keyLength, BYTE[] data, dword dataLength, BYTE[] initVector, dword initVectorLength, BYTE[] cipheredData, dword cipheredDataLength)
```

## Description

Encrypts data with a given key and initialization vector. The encryption is AES128 (CBC), PKCS5 Padding.

## Availability

| Up to Version |
|---|
