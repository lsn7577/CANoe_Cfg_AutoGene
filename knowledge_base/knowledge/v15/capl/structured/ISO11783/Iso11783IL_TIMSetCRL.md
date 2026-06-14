# Iso11783IL_TIMSetCRL

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetCRL(byte crlType, char crlFilePath[]); // form 1
long Iso11783IL_TIMSetCRL(dbNode participant, byte crlType, char crlFilePath[]); // form 2
```

## Description

Loads a Certificate Revocation List file which is used for TIM authentication. If there is already a loaded certificate file for a certificate type these file is overwritten.

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| 0 | Certificate Revocation List for Testlab, Manufacturer, manufacturer series, TIM client and TIM server certificates. |
| 1 | Certificate Revocation List for the CRL signing CA certificates. |
| crlFilePath | Path of a CRL file (DER file format). Path has to be absolute or relative relating to the folder of the CANoe configuration. |
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
