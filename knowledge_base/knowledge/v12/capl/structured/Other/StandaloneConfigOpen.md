# StandaloneConfigOpen

> Category: `Other` | Type: `function`

## Syntax

```c
dword StandaloneConfigOpen(CHAR rtcfgFileName[], dword stopCurrentMeasurement, dword startNewMeasurement, dword returnToActiveConfig)
```

## Description

Opens the RTCFG file with the given name as standalone configuration.

## Return Values

The function returns an error code with 0 representing successful operation.

## Example

```c
// "Config1.RTCFG" (master config.) contains following CAPL code:

on key F2
{
   StandaloneConfigOpen("Config2.RTCFG", 1, 1, 1);
}
on key F3
{
   StandaloneConfigOpen("Config3.RTCFG", 1, 0, 1);
}
```

## Availability

| Since Version |
|---|
