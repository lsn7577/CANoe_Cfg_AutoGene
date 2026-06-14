# J1939ILControlStop

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILControlStop(); // form 1
long J1939ILControlStop(dbNode node); // form 2
long J1939ILControlStop( dword options ); // form 3
long J1939ILControlStop(dbNode node, dword options ); // form 4
```

## Description

Deactivates the IL and stops sending cyclic messages.

A Cannot Claim Address message is sent, if the NMT is activated and the message is not suppressed with the parameter option set to 1.

## Parameters

| Name | Description |
|---|---|
| options | options1: suppress sending Cannot Claim Address message |
| node | Simulation node to apply the function |

## Return Values

0 on success or IL Error Code

## Example

```c
on key 's'
{
J1939ILControlStop(1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2: form 1, 3 12.0: form 2, 4 | 13.0 | — | — | 4.0 |
| Restricted To | — | J1939 | J1939 | — | — | form 2, 4 J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3) | ✔ (form 1, 3) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
