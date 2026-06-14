# StandaloneGetCurrentConfig

> Category: `Other` | Type: `function`

## Syntax

```c
dword StandaloneGetCurrentConfig(char cfgNameBuffer[], dword cfgNameBufferLength);
```

## Description

Returns the file name of the currently loaded configuration in standalone mode. It includes the file extension, but no path information, for example CANSystemDemo.rtcfg.

The function can be used in standalone mode. It is also useful to determine whether standalone mode is active or not.

## Parameters

| Name | Description |
|---|---|
| cfgNameBuffer | Space for the returned name. |
| cfgNameBufferLength | Length of the buffer. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 | 8.2 | 13.0 | — | 14 | 1.1 |
| Restricted To | Standalone mode | Standalone mode | Standalone mode | — | Standalone mode | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
