# TCIL_ConnectSysVarWithDataEntity

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ConnectSysVarWithDataEntity(dbNode client, dword ddi, dword elementNumber, char[]sysVarNameWithPath, dword useRawValue); // form 1
long TCIL_ConnectSysVarWithDataEntity(dword addressClient, dword ddi, dword elementNumber, char[]sysVarNameWithPath, dword useRawValue); // form 2
long TCIL_ConnectSysVarWithDataEntity(dbNode tc, dbNode client, dword ddi, dword elementNumber, char[]sysVarNameWithPath, dword useRawValue); // form 3
long TCIL_ConnectSysVarWithDataEntity(dbNode tc, dword addressClient, dword ddi, dword elementNumber, char[]sysVarNameWithPath, dword useRawValue); // form 4
```

## Description

This function connects a data entity specified by the data dictionary identifier to a system variable.

If the value of the data entity is changed, the new value is put into the system variable. To release connection between the system variable and data entity, just call the same method again, but with the empty string instead of the name of system variable.

## Parameters

| Name | Description |
|---|---|
| ddi | Data dictionary identifier of the data entity, 0x0000..0xFFFF. |
| elementNumber | Element number of the data entity, 0x000..0xFFF. |
| sysVarNameWithPath | Name of the system variable, all name spaces inclusive. |
| useRawValue | 1: The connected system variable represents the raw value of data entity. This variant can be used even if the corresponding device descriptor object pool is not uploaded to the Task Controller simulated by TC IL. 0: The connected system variable represents the physical value of data entry. Precondition: The corresponding device descriptor object pool has to be uploaded to Task Controller simulated by TC IL and the data entry belongs to the device descriptor object pool. |
| client | Task Controller client which provides the device descriptor object pool with corresponding data entity. |
| addressClient | Address of the Task Controller client which provides the device descriptor object pool with corresponding data entity. |
| tc | Task Controller simulation node to apply the function. |

## Example

Example form 3

```c
result = TCIL_ConnectSysVarWithDataEntity(TC, Sprayer, 117, 1, "Sprayer::svEffectiveTotalDistance", 1);
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
