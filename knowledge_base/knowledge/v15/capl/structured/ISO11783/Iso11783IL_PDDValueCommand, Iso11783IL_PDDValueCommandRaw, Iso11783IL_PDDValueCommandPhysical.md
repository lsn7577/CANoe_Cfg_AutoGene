# Iso11783IL_PDDValueCommand, Iso11783IL_PDDValueCommandRaw, Iso11783IL_PDDValueCommandPhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDD ValueCommand (dword ddi, dword elementNumber); //form 1
long Iso11783IL_PDD ValueCommand(dbNode implement, dword ddi, dword elementNumber); //form 2
long Iso11783IL_PDD ValueCommandRaw(dword ddi, dword elementNumber, long value); //form 3
long Iso11783IL_PDD ValueCommandRaw(dbNode implement, dword ddi, dword elementNumber, long value); //form 4
long Iso11783IL_PDD ValueCommandPhysical(dword ddi, dword elementNumber, double value); //form 5
long Iso11783IL_PDD ValueCommandPhysical(dbNode implement, dword ddi, dword elementNumber, double value); //form 6
```

## Description

Form (1) and (2) send the current value of the specified data entity to the Task Controller with Value command. It can be used to send to the Task Controller the previously set Compressed State DDIs (using Iso11783IL_PDDSetValueRaw or Iso11783IL_PDDSetValuePhysical).

Form (3)-(6) set the value to the specified data entity (if exists) and sends the value to the Task Controller with Value command.

## Parameters

| Name | Description |
|---|---|
| ddi | Data Dictionary Identifier, 0x0000.0xFFFF |
| elementNumber | Element number, 0x000.0xFFF |
| value | New value of the data entity (process variable) |
| implement | Task Controller simulation node to apply the function. |

## Example

Example form 2

```c
void ReportActualStateOfSomeSections()
{
  long result;

  // Sections 1, 3, 20 and 21 are enabled
  // All sections belong to the elementNumber=7
  //the first two sections belong to the DDI=161
  //the last two sections belong to the DDI=162
  Iso11783IL_PDDSetSectionState(Sprayer, 161, 7, 1, 1);
  Iso11783IL_PDDSetSectionState(Sprayer, 161, 7, 3, 1);
  Iso11783IL_PDDSetSectionState(Sprayer, 162, 7, 20, 1);
  Iso11783IL_PDDSetSectionState(Sprayer, 162, 7, 21, 1);

  //each DDI has to be sent with a single command
  //the first two sections belong to the DDI=161
  Iso11783IL_PDDValueCommand(Sprayer, 161, 7);
  //the last two sections belong to the DDI=162
  Iso11783IL_PDDValueCommand(Sprayer, 162, 7);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2, 4, 6 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3, 5) | ✔ (form 1, 3, 5) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4, 6) | ✔ (form 2, 4, 6) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4, 6) | ✔ (form 2, 4, 6) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
