# TCIL_GetSectionState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetSectionState (dbNode client, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, dword& sectionState); // form 1
long TCIL_GetSectionState (dword addressClient, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, dword& sectionState); // form 2
long TCIL_GetSectionState (dbNode tc, dbNode client, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, dword& sectionState); // form 3
long TCIL_GetSectionState (dbNode tc, dword addressClient, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, dword& sectionState); // form 4
```

## Description

These functions return the current state of a single section.

For the already specified DDIs (currently in range DDI=0 and DDI=520), the functions check if the sectionNumber fits to the DDI.

## Parameters

| Name | Description |
|---|---|
| tc | Task Controller simulation node to apply the function. |
| client | Task Controller client node the data entity belongs to. |
| addressClient | Address of Task Controller client node the data entity belongs to. |
| elementNumber | Element number, 0x000..0xFFF. |
| ddiOfCondensedState | Data dictionary identifier the condensed state belongs to, e.g.: 161..176 (0x0A1..0x0B0) for Actual Condensed Work State 290..305 (0x122..0x131) for Setpoint Condensed Work State 367..382 (0x16F..0x17E) for Condensed Section Override State 517 (0x205) for Setpoint Tramline Condensed Work State 1-16 518 (0x206) for Actual Tramline Condensed Work State 1-16 |
| sectionNumber | Section number within the object, 1..256. |
| sectionState | New section state, 0..3. 0: disabled/off 1: enabled/on 2: error indicator 3: no change |

## Example

Example form 3

```c
dword IsSectionEnabled(dword elementNumber, dword sectionNumber)
{
  long result;
  dword state;
  result = TCIL_GetSectionState(TC, Sprayer, 161, elementNumber, sectionNumber, state);
  if (result < 0)
  {
    TestStepFail("Failed to get current state!");
    return result;
  }
  return (state == 1);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2: form 1, 3 13.0: form 2, 4 | 13.0 | — | — | 2.1: form 3 5.0: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
