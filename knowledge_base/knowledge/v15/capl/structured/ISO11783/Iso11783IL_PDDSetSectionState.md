# Iso11783IL_PDDSetSectionState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDSetSectionState(dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, dword sectionState); // form 1
long Iso11783IL_PDDSetSectionState(dbNode implement, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, dword sectionState); // form 2
```

## Description

Sets the state of a single section.

For the already specified DDIs (currently in range DDI=0 and DDI=520), the functions check if the sectionNumber fits to the DDI.

## Parameters

| Name | Description |
|---|---|
| ddiOfCondensedState | Data dictionary identifier the condensed state belongs to, e.g.: 161..176 (0x0A1..0x0B0) for Actual Condensed Work State 290..305 (0x122..0x131) for Setpoint Condensed Work State 367..382 (0x16F..0x17E) for Condensed Section Override State 517 (0x205) for Setpoint Tramline Condensed Work State 1-16 518 (0x206) for Actual Tramline Condensed Work State 1-16 |
| elementNumber | Element number, 0x000..0xFFF. |
| sectionNumber | Section number within the object, 1..256. |
| sectionState | 0: disabled/off 1: enabled/on 2: error indicator 3: no change |
| implement | Simulation node to apply the function. |

## Example

```c
long result;
char text[256];
result = Iso11783IL_PDDSetSectionState(290, 10, 1, 1);
if (result < 0)
{
  Iso11783IL_PDDGetLastErrorText ( elCount(text), text );
  write( "ERROR: %s", text);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP3: form 1 9.0 SP3: form 2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
