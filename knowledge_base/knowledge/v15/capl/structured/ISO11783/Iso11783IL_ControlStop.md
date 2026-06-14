# Iso11783IL_ControlStop

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_ControlStop(); // form 1
long Iso11783IL_ControlStop( dword option ); // form 2
long Iso11783IL_ControlStop( dbNode node ); // form 3
long Iso11783IL_ControlStop( dbNode node, dword option ); // form 4
```

## Description

Deactivates the IL and stops sending cyclic messages. A Cannot Claim Address message is sent, if the NMT is activated and the message is not suppressed with the parameter option set to 1.

## Parameters

| Name | Description |
|---|---|
| option | Options1: Suppress sending Cannot Claim Address message. |
| node | Simulation node to apply the function. |

## Return Values

0 on success or error code

## Example

```c
on key 's'
{
Iso11783IL_ControlStop(1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1, 2 11.0 SP2: form 3, 4 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
