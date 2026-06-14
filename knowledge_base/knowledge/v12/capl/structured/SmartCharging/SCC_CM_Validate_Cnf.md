# SCC_CM_Validate_Cnf

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CM_Validate_Cnf ( byte RunId[], byte SourceMacAddress[], dword Result, dword ToggleNum )
```

## Description

The callback is called as soon as a CM_Validate.Cnf message is received. Further details (signal type) that are transmitted in this request can be queried with SCC_SLAC_GetSignalType.

## Return Values

—

## Availability

| Since Version |
|---|
