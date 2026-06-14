# StandaloneConfigOpen

> Category: `Other` | Type: `function`

## Syntax

```c
dword StandaloneConfigOpen(CHAR rtcfgFileName[], dword stopCurrentMeasurement, dword startNewMeasurement, dword returnToActiveConfig)
```

## Description

Opens the RTCFG file with the given name as standalone configuration.

## Parameters

| Name | Description |
|---|---|
| rtcfgFileName | Name of the standalone configuration file (without path) to be set as default file. |
| stopCurrentMeasurement | If this parameter is 1 measurement is stopped immediately (but still waiting for deferred stop clients). If the parameter value is 0 the request to load another configuration is queued until end of measurement. |
| startNewMeasurement | If this parameter is set to 1 measurement will start immediately after the new configuration has been loaded. |
| returnToActiveConfig | If this parameter is set to 1 the default configuration (usually a sort of “master configuration”) will be loaded automatically after measurement based on the new configuration will have been stopped. |

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
