# Iso11783IL_TIMSetCertificateSequence

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetCertificateSequence(dword certificateType1, dword certificateType2, dword certificateType3, dword certificateType4); // form 1
long Iso11783IL_TIMSetCertificateSequence(dbNode participant, dword certificateType1, dword certificateType2, dword certificateType3, dword certificateType4); // form 2
```

## Description

Sets the sequence of requested certificates.

Use this function to change the sequence of requested certificates. By default the following sequence is used:

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| 1 | Testlab certificate |
| 2 | Manufacturer certificate |
| 3 | Manufacturer series certificate |
| 4 | Device certificate |
| certificateType2 | Type of second requested certificate. Default value: 2 (Manufacturer certificate). |
| certificateType3 | Type of third requested certificate. Default value: 3 (Manufacturer series certificate). |
| certificateType4 | Type of fourth requested certificate. Default value: 4 (Device certificate). |
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
