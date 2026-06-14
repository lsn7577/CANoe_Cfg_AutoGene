# SecurityLocalEncryptAES128CBC

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalEncryptAES128CBC(byte key[], dword keyLength, byte data[], dword dataLength, byte initVector[], dword initVectorLength, byte cipheredData[], dword cipheredDataLength)
```

## Description

Encrypts data with a given key and initialization vector using AES128 (CBC), Padding Mode PKCS5.

## Return Values

1: SuccessA Value of 1 means that the action was successful.

## Availability

| Since Version |
|---|
