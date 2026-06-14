# SCC_CM_Set_Key_Cnf

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_CM_Set_Key_Cnf ( byte RunId[], byte SourceMacAddress[], dword Result )
```

## Description

The callback is called as soon as a CM_Set_Key.Cnf message is received. Further details that are transmitted in this request can be queried with SCC_SLAC_GetCMSetKeyCnfData.

## Return Values

—

## Availability

| Since Version |
|---|
