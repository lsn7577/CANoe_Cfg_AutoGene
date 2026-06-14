# SCC_VS_PL_Lnk_Status_Cnf

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
void SCC_VS_PL_Lnk_Status_Cnf ( byte SourceMacAddress[], dword MStatus, dword LinkStatus )
```

## Description

The callback is called as soon as a VS_PL_Lnk_Status.Cnf message is received. This is the response of the QCA9000 chip when using link status polling. (Additional data cannot be queried at the moment.)

## Return Values

—

## Availability

| Since Version |
|---|
