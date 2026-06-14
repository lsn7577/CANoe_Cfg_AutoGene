# diagCheckValidNegResCode

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagCheckValidNegResCode( diagRequest obj, dword negResCode);
long diagCheckValidNegResCode( diagResponse obj, dword negResCode);
long diagCheckValidNegResCode( diagResponse obj);
```

## Description

The functions return 1 if the given negative response code is defined for the object. It returns 0 if the code is not valid, and <0 for an error.

In the one-argument form, the response object has to be a negative response.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object to check the response code for. |
| negResCode | Negative response code like 0x11, "serviceNotSupported" (KWP 2000). |

## Return Values

Error code

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 5.2 7.0 SP5: methods | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
