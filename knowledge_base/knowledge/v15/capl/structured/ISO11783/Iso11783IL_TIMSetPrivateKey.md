# Iso11783IL_TIMSetPrivateKey

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetPrivateKey(char privateKeyFilePath[]); // form 1
long Iso11783IL_TIMSetPrivateKey(dbNode participant, char privateKeyFilePath[]); // form 2
```

## Description

Loads an ECC private key file which is used for TIM authentication. If there is already a private key then it is overwritten.

## Parameters

| Name | Description |
|---|---|
| privateKeyFilePath | Path of a private key file which contains a hexadecimal representation of the private key. Path has to be absolute or relative relating to the folder of the CANoe configuration. |
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
