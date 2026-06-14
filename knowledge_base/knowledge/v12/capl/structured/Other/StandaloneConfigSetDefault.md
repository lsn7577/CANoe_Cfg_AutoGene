# StandaloneConfigSetDefault

> Category: `Other` | Type: `function`

## Syntax

```c
dword StandaloneConfigSetDefault(CHAR rtcfgFileName[])
```

## Description

Changes the default configuration file, i.e. the standalone configuration to be loaded when standalone mode is activated or the runtime kernel is started after reboot. Thus, it results in a persistent change on the VN8900.

## Return Values

The function returns an error code with 0 representing successful operation.

## Availability

| Since Version |
|---|
