# writeEx

> Category: `Other` | Type: `function`

## Syntax

```c
void writeEx(long sink, dword severity, char format[], ...);
```

## Description

Writes the text into the last line of the specified CANoe window, into a page of the Write Window or into a logging file without previously creating a new line.

To write into the CANoe Trace Window please activate the CAPL System Message in the predefined filters of the Trace Window.

## Parameters

| Name | Description |
|---|---|
| -3 | Trace Window |
| -2 | Output to the logging file (only in ASC format and if the CAPL node is inserted in the Measurement Setup in front of the Logging Block) |
| -1 | Reserved |
| 0 | Output to the System page of the Write Window |
| 1 | Output to the CAPL page of the Write Window |
| 4 | Output to the Test page of the Write Window |
| 0 | Success |
| 1 | Information |
| 2 | Warning |
| 3 | Error |
| format | Formatting character sequence. |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.2 | 3.2 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
