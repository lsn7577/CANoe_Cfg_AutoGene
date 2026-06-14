# on a429worderror

> Category: `A429` | Type: `event`

## Description

The event procedure on a429worderror is called on every event, related to an ARINC word error. The error type is available in the selector error.

Note that there are errors without any valid label information. This is especially the gap violation error. The ARINC word causing that error triggers a on a429word procedure. For this reason it makes sense to catch all errors in a single channel related handler.

ARINC word errors are also monitored with statistics system variables.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | — | — | — | — |
| Restricted To | A429 | A429 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |

## Selectors

| a429word | More information about a429word. |
|---|---|
| a429word | ../CAPLfunctionsA429DefineARINCword.htm |
