# SCC_GetDLLInfo

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
dword SCC_GetDLLInfo ( dword selector )
```

## Description

This function returns additional information to the DLL.

## Return Values

Selector
Description of return value
0
The file version of the DLL in BCD format, e.g., 0x010203 for V1.2.3
1
The main version of the DLL
2
The subversion of the DLL
3
The build number of the DLL

## Availability

| Since Version |
|---|
