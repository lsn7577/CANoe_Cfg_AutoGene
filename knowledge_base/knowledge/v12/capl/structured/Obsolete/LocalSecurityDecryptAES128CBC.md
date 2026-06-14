# LocalSecurityDecryptAES128CBC

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long LocalSecurityDecryptAES128CBC(BYTE[] key, dword keyLength, BYTE[] cipheredData, dword cipheredData Length, BYTE[] initVector, dword initVectorLength, BYTE[] plainData, dword plainData Length)
```

## Description

Decrypts data with a given key and initialization vector. The decryption is AES128 (CBC), PKCS5 Padding.

## Availability

| Up to Version |
|---|
