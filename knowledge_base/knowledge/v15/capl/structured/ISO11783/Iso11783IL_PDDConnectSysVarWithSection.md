# Iso11783IL_PDDConnectSysVarWithSection

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDConnectSysVarWithSection(dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, char[] sysVarNameWithPath); // form 1
long Iso11783IL_PDDConnectSysVarWithSection(dbNode implement, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, char[] sysVarNameWithPath); // form 2
```

## Description

Connects a single section state to a system variable.

If a section state is changed the new value is put into the system variable.

To release connection between the system variable and the condensed state, just call the same method again, but with the empty string instead of the name of system variable.

## Parameters

| Name | Description |
|---|---|
| ddiOfCondensedState | Data dictionary identifier the condensed state belongs to, e.g.: 161..176 (0x0A1..0x0B0) for Actual Condensed Work State 290..305 (0x122..0x131) for Setpoint Condensed Work State 367..382 (0x16F..0x17E) for Condensed Section Override State |
| elementNumber | Element number, 0x000..0xFFF. |
| sectionNumber | Section number within the object, 1..256. |
| sysVarNameWithPath | Name of the system variable, all name spaces inclusive. |
| implement | Simulation node to apply the function. |

## Example

```c
long result;
char text[256];
result = Iso11783IL_PDDConnectSysVarWithSection(290, 10, 1, "ConnectedSysVars::svSection1");
if (result < 0)
{
  Iso11783IL_GetLastErrorText ( elCount(text), text );
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
