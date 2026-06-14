# SCC_SetTLSEnabled

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_SetTLSEnabled ( long Enabled )
```

## Description

Specifies if TLS is used. As native TLS is not supported, this only affects the Security flag in the SECC Discovery Request message. By calling this function, the configuration parameter <UseTLS> is overwritten.

## Return Values

—

## Availability

| Since Version |
|---|
