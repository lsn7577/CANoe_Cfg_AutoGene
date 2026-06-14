# LocalSecurityEncryptAES128ECB

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long LocalSecurityEncryptAES128ECB(BYTE[] key, dword keyLength, BYTE[] data, dword dataLength, BYTE[] cipheredData, dword cipheredDataLength)
```

## Description

Encrypts data with a given key and initialization vector. The encryption is AES128 (ECB), PKCS5 Padding. ECB Mode does not use an initialization vector.

## Availability

| Up to Version |
|---|
