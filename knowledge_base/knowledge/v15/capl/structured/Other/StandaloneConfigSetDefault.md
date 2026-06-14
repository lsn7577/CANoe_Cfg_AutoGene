# StandaloneConfigSetDefault

> Category: `Other` | Type: `function`

## Syntax

```c
dword StandaloneConfigSetDefault(CHAR rtcfgFileName[]);
```

## Description

Changes the default configuration file, i.e. the standalone configuration to be loaded when standalone mode is activated or the RT kernel is started after reboot. Thus, it results in a persistent change on the VN8900.

## Parameters

| Name | Description |
|---|---|
| rtcfgFileName | Name of the standalone configuration file (without path) to be set as default configuration file. |

## Return Values

The function returns an error code with 0 representing successful operation.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.6 SP3 | 7.6 SP3 | 13.0 | — | 14 | 1.0 |
| Restricted To | Standalone mode | Standalone mode | Standalone mode | — | Standalone mode | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
