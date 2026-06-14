# getConfigurationName

> Category: `Other` | Type: `function`

## Syntax

```c
long getConfigurationName(char buffer[], dword bufferLength);
```

## Description

Returns the file name of the currently loaded configuration. It includes neither the file extension nor any path information, for example CANSystemDemo.

## Parameters

| Name | Description |
|---|---|
| buffer | Space for the returned name. |
| bufferLength | Length of the buffer. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | 13.0 | — | 14 | 2.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
