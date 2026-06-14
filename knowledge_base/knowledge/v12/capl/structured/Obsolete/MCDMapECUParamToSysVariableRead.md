# MCDMapECUParamToSysVariableRead

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long MCDMapECUParamToSysVariableRead(char moduleName[], char parameterName[], SysVarName)
```

## Description

Maps an ECU parameter to a system variable so that it the system variable changes whenever the parameter is updated. The MCD data acquisition must already be started.

## Return Values

0: No error.

## Availability

| Up to Version |
|---|
