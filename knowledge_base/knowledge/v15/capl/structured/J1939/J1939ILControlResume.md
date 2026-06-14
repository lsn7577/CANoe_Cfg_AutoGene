# J1939ILControlResume

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILControlResume(); // form 1
long J1939ILControlResume(dbNode node); // form 2
```

## Description

After suspending the J1939 IL with J1939ILControlWait, this function restarts the IL. The J1939 IL starts sending cyclic messages again.

## Parameters

| Name | Description |
|---|---|
| node | Simulation node to apply the function |

## Return Values

0 on success or IL Error Code

## Example

```c
on key 'r'
{
J1939ILControlResume();
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2: form 1 12.0: form 2 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 | J1939 | — | — | form 2 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
