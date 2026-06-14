# ChkConfig_Init

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkConfig_Init (char aRole[]); // form 1: deprecated
long ChkConfig_Init (); // form 2
```

## Description

Initializes TSL to be used subsequently.

If the function is used, then it is recommended to perform the initialization once during preStart section of the CAPL program.

The tester role (form 1) has no longer an effect.

## Parameters

| Name | Description |
|---|---|
| aRole | Allowed value range: developer, user |

## Example

```c
// test is executed in the role of a developer
on preStart
{
   ChkConfig_Init();
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0-8.5 SP2: form 1 8.5 SP3: form 2 | 13 | 13 | 14 | 1.0-2.0: form 1 2.0 SP2: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
