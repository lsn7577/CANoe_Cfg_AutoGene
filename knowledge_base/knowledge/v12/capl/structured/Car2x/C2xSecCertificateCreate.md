# C2xSecCertificateCreate

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateCreate(long originalCertificateHandle, dword validityInSeconds);
```

## Description

Generate a new certificate based on another certificate.

The certificate is only valid while the measurement is running and it is automatically discarded afterwards.

The certificate is only known to the real-time part of CANoe. The analysis part only gets knowledge of it when it is transmitted in a message.

## Return Values

Handle of the new certificate or 0 on failure

## Availability

| Since Version |
|---|
