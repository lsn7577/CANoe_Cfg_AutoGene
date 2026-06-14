# Iso11783IL_TIMAddCertificate

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMAddCertificate(byte certificateType, char certificateFilePath[]); // form 1
long Iso11783IL_TIMAddCertificate(dbNode participant, byte certificateType, char certificateFilePath[]); // form 2
```

## Description

Loads a certificate file which is used for TIM authentication. If there is already a loaded certificate file for a certificate type these file is overwritten.

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| 0 | AEF Root certificate |
| 1 | Testlab certificate |
| 2 | Manufacturer certificate |
| 3 | Manufacturer series certificate |
| 4 | Device certificate |
| 5 | CRL signing certificate |
| certificateFilePath | Path of a certificate file (DER file format). Path has to be absolute or relative relating to the folder of the CANoe configuration. |
| participant | TIM participant (TIM server or TIM client). |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
