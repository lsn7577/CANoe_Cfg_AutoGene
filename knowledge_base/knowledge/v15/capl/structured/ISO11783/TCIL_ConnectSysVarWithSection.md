# TCIL_ConnectSysVarWithSection

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ConnectSysVarWithSection(dbNode client, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, char[] sysVarNameWithPath); // form 1
long TCIL_ConnectSysVarWithSection(dword addressClient, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, char[] sysVarNameWithPath); // form 2
long TCIL_ConnectSysVarWithSection(dbNode tc, dbNode client, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, char[] sysVarNameWithPath); // form 3
long TCIL_ConnectSysVarWithSection(dbNode tc, dword addressClient, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, char[] sysVarNameWithPath); // form 4
```

## Description

This function connects a single section state to a system variable.

If a section state is changed the new value is put into the system variable. To release connection between the system variable and the condensed state, just call the same method again, but with the empty string instead of the name of system variable.

## Parameters

| Name | Description |
|---|---|
| ddiOfCondensedState | Data dictionary identifier the condensed state belongs to, e.g.: 161..176 (0x0A1..0x0B0) for Actual Condensed Work State 290..305 (0x122..0x131) for Setpoint Condensed Work State 367..382 (0x16F..0x17E) for Condensed Section Override State |
| elementNumber | Element number of the data entity, 0x000..0xFFF. |
| sectionNumber | Section number within the object, 1..256. |
| sysVarNameWithPath | Name of the system variable, all name spaces inclusive. |
| client | Task Controller client which provides the device descriptor object pool with corresponding sections. |
| addressClient | Address of the Task Controller client which provides the device descriptor object pool with corresponding sections. |
| tc | Task Controller simulation node to apply the function. |

## Example

Example form 2

```c
long result;
result = TCIL_ConnectSysVarWithSection(TC, Sprayer, 162, 1, 20,
Sprayer::svActualCondensedWorkStateSection20");
switch (result)
{
  case     0: TestStepPass(); break;
  case -2203: TestStepFail("Invalid system variable path!"); break;
  case -2211: TestStepFail("System variable does not exist!"); break;
  default   : TestStepFail("Unexpected error!"); break;
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP4: form 1, 3 13.0: form 2, 4 | 13.0 | — | — | 2.1 SP4: form 3 5.0: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
