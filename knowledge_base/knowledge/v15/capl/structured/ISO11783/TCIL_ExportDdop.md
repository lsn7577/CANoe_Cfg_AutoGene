# TCIL_ExportDdop

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ExportDdop(dbNode client, char ddopPath[]); // form 1
long TCIL_ExportDdop(dword addressClient, char ddopPath[]); // form 2
long TCIL_ExportDdop(dbNode tc, dbNode client, char ddopPath[]); // form 3
long TCIL_ExportDdop(dbNode tc, dword addressClient, char ddopPath[]); // form 4
```

## Description

Exports the device descriptor object pool of the Task Controller client into a file.

## Parameters

| Name | Description |
|---|---|
| client | Task Controller client which provides the device descriptor object pool with corresponding sections. |
| addressClient | Address of the Task Controller client which provides the device descriptor object pool with corresponding sections. |
| tc | Task Controller simulation node to apply the function. |
| ddopPath | Path of the target DDOP file (*.xml). |

## Example

Example form 3

```c
Example (*)
long result;
result =  TCIL_ExportDdop( TC, Sprayer, "xml\\sprayerV1.xml");
if (result < 0)
{
  TestStepFail("Failed to export DDOP!");
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
