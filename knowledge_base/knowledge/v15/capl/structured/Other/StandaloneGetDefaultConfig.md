# StandaloneGetDefaultConfig

> Category: `Other` | Type: `function`

## Syntax

```c
dword StandaloneGetDefaultConfig(char cfgNameBuffer[], dword cfgNameBufferLength);
```

## Description

Gets the name of the default configuration in standalone mode. This is the standalone configuration, which gets loaded when standalone mode is activated or the RT kernel is started after reboot.

The command can be used while standalone mode is running. It is also useful to determine whether standalone mode is running or not.

A returned configuration name consists of the file name and the extension, for example CANSystemDemo.rtcfg.

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
  cfgRet=StandaloneGetDefaultConfig(cfgName,elcount(cfgName));
  write("StandaloneGetDefaultConfig returns %d %s",cfgRet,cfgName);
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
