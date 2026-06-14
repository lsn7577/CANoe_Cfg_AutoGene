# Iso11783OPOnSelectInput

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783OPOnSelectInput( dword ecuHandle, dword objectID, dword what );
```

## Description

The function is called by the node layer, if an input object is selected.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU |
| objectID | Object ID of the selected input object |
| what | 0: input object is not selected 1: input object is selected 2: input object is opened |

## Return Values

—

## Example

```c
void Iso11783OPOnSelectInput( dword handle, dword objectID, dword what )
{
}
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
