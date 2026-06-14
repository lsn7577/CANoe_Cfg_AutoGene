# SecurityLocalGenerateCMAC

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalGenerateCMAC(byte key[], dword keyLength, byte data[], dword dataLength, byte cmac[], dword cmacLength)
```

## Description

Generates a hash for the given data and key. The generated hash is a CMAC.

## Return Values

1: SuccessA Value of 1 means that the action was successful.

## Availability

| Since Version |
|---|
