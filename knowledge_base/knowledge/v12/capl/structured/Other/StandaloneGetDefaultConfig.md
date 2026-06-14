# StandaloneGetDefaultConfig

> Category: `Other` | Type: `function`

## Syntax

```c
dword StandaloneGetDefaultConfig(char cfgNameBuffer[], dword cfgNameBufferLength)
```

## Description

Gets the name of the default configuration in standalone mode. This is the standalone configuration, which gets loaded when standalone mode is activated or the runtime kernel is started after reboot.

The command can be used while standalone mode is running. It is also useful to determine whether standalone mode is running or not.

A returned configuration name consists of the file name and the extension, for example CANSystemDemo.rtcfg.

## Return Values

0: Successful operation

## Example

```c
on start
{
  char cfgName[200];
  DWORD cfgRet;
  cfgName[0]=0;
  cfgRet=StandaloneGetDefaultConfig(cfgName,elcount(cfgName));
  write("StandaloneGetDefaultConfig returns %d %s",cfgRet,cfgName);
}
```

## Availability

| Since Version |
|---|
