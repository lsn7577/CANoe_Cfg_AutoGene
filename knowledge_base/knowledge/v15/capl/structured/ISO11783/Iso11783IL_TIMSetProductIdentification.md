# Iso11783IL_TIMSetProductIdentification

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetProductIdentification(char identification[]); // form 1
long Iso11783IL_TIMSetProductIdentification(dbNode participant, char identification[]); // form 2
```

## Description

Sets the content of message Product identification (see ISO11783-12 B.10).

If the Product identification message is in the Tx list of the TIM node and a request for PGN 65242 (FC8Dh) is received then the Product identification message is sent using the data of parameter identification.

## Parameters

| Name | Description |
|---|---|
| identification | Content of the Product information message. Format of the string must be <product identification code>*<product identification brand>*<product identification model>* If this parameter is an empty string then no Product identification information message is sent on a request. To answer the request with another message (e.g. an Acknowledgement message) you can use ISO11783IL_OnRequest. |
| participant | TIM participant (TIM server or TIM client). |

## Example

```c
Iso11783IL_TIMSetProductIdentification (“1234567890ABC*Brand B*1962i*”);
```

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
