# getConfigurationName

> Category: `Other` | Type: `function`

## Syntax

```c
long getConfigurationName(char buffer[], dword bufferLength);
```

## Description

Returns the file name of the currently loaded configuration. It includes neither the file extension nor any path information, for example CANSystemDemo.

There are two kinds of configurations in standalone mode:

These two file names may well differ (even though normally they are the same except for the file extension).

StandaloneGetCurrentConfig returns the standalone configuration file name, whereas getConfigurationName returns the normal configuration file name.

## Return Values

-1 Buffer too small

## Example

```c
on start
{
  char cfgName[260];
  dword ret;
  ret = getConfigurationName(cfgName,elcount(cfgName));
  write("getConfigurationName returns %d %s", ret, cfgName);
}
```

## Availability

| Since Version |
|---|
