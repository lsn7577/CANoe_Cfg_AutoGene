# Iso11783IL_ControlInit

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_ControlInit(); // form 1
long Iso11783IL_ControlInit( byte deviceName[8] ); // form 2
long Iso11783IL_ControlInit( dbNode node ); // form 3
long Iso11783IL_ControlInit( dbNode node, byte deviceName[8] ); // form 4
```

## Description

This function can only be used in on preStart, to suppress the auto-start function of the IL.

If the device name is not specified, the node attributes with the device name must be defined (Exception: If NMT is not activate, the device name is not needed).

## Parameters

| Name | Description |
|---|---|
| deviceName | ISO11783 64-Bit device name (optional). |
| node | Simulation node to apply the function. |

## Return Values

0 on success or error code

## Example

```c
on preStart
{
Iso11783IL_ControlInit();
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
