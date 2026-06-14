# StandaloneGetCurrentConfig

> Category: `Other` | Type: `function`

## Syntax

```c
dword StandaloneGetCurrentConfig(char cfgNameBuffer[], dword cfgNameBufferLength)
```

## Description

Returns the file name of the currently loaded configuration in standalone mode. It includes the file extension, but no path information, for example CANSystemDemo.rtcfg.

The function can be used in standalone mode. It is also useful to determine whether standalone mode is active or not.

There are two kinds of configurations in standalone mode:

These two file names may well differ (even though normally they are the same except for the file extension).

StandaloneGetCurrentConfig returns the standalone configuration file name, whereas getConfigurationName returns the normal configuration file name.

## Return Values

0: Successful operation

## Example

```c
on start
{
  char cfgName[200];
  DWORD cfgRet;
  cfgName[0]=0;
  cfgRet=StandaloneGetCurrentConfig(cfgName,elcount(cfgName));
  write("StandaloneGetCurrentConfig returns %d %s",cfgRet,cfgName);
}
```

## Availability

| Since Version |
|---|
