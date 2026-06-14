# coTfsSetApplProfile

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetApplProfile( dword profile );
```

## Description

The function enables the support of an application profile. The function has to be called before any test functions are executed.

## Parameters

| Name | Description |
|---|---|
| profile | Number of profile which is to be set, the values 0 and 301 are saved as 301 and represent the default value. |

## Return Values

Error code

## Example

```c
coTfsSetApplProfile(447);

//...

coTfsSetApplProfile(301); // set back to default
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
