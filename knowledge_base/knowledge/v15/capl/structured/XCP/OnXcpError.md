# OnXcpError

> Category: `XCP` | Type: `function`

## Syntax

```c
void OnXcpError (char ecuQualifier[], byte xcpCmd, byte xcpErrorCode);
```

## Description

Whenever the XCP slaves answers with a negative response (i.e. not 0xFF) the OnXCPError callback function is called.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Name of the device, configured within the CANoeXCP/CCP Window. |
| xcpCmd | XCP command sent by CANoe. |
| xcpErrorCode | Error code returned by the XCP slave. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | XCP | XCP | — | — | XCP |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
