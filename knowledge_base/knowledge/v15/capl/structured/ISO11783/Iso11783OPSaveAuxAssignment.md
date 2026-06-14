# Iso11783OPSaveAuxAssignment

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPSaveAuxAssignment( dword ecuHandle, char filename[] );
```

## Description

The function saves the current auxiliary input assignment as "Preferred Auxiliary Input Assignment" in an ini file.

With the function Iso11783OPLoadAuxAssignment the "Preferred Assignment" can be load and used again.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU. |
| filename | File name of an ini file (*.INI) |

## Return Values

0 or error code

## Example

```c
dword handle = 0;
handle = Iso11783CreateECU( gECUName );
[...]
Iso11783OPSaveAuxAssignment( handle, "Sprayer.INI");
[...]
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
