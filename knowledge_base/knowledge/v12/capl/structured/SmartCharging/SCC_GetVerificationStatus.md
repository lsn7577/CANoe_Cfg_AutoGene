# SCC_GetVerificationStatus

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
dword SCC_GetVerificationStatus ( )
```

## Description

Returns the state of the received message regarding the validity of its signature.

## Return Values

0 = Verification failed
1 = Verification successful
2 = Not verified (unsigned message or not required)

## Availability

| Since Version |
|---|
