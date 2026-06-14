# SecurityLocalEncryptAES128ECB

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalEncryptAES128ECB(byte key[], dword keyLength, byte data[], dword dataLength, byte cipheredData[], dword cipheredDataLength)
```

## Description

Encrypts data with a given key using AES128 (ECB), Padding Mode PKCS5.

## Return Values

1: SuccessA Value of 1 means that the action was successful.

## Availability

| Since Version |
|---|
