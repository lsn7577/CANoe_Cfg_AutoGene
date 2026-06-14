# Iso11783IL_PDDSetParameter

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDSetParameter( char paramName[], float paramValue ); // form 1
long Iso11783IL_PDDSetParameter( dbNode simulNode, char paramName[], float paramValue ); // form 2
```

## Description

Changes an internal parameter of the PDD API.

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| debug | activates debug outputs in the Write Window 1: on 0: off |
| autoUpdateVariable | process variable is updated if value command is received 1: auto update 0: process variable have to be updated manually by Iso11783IL_PDDSetValue e.g. in callback function Iso11783IL_PDDOnDataChanged |
| Note Using version the version value obtained from the database (node attribute ISO11783PDDVersion) is overwritten. |  |
| Value | Description |
| BootTimeTC" | maximum number of seconds from a power cycle to transmission of the first Task Controller Status message, default: 255 |
| ImplementSectionControl | 1: supports implement section control default: doesn’t support. |
| PeerControlAssignment | 1: supports peer control assignment default: doesn’t support |
| TC_GEO_DefinitionPositionBasedControl | 1: TC-GEO definition, position based control default: doesn’t support. |
| TimeAndPositionForDataLogging | 1: supports time and position for data logging default: doesn’t support |
| Documentation | 1: supports documentation default: doesn’t support |
| NumberOfBooms | minimum required number of booms that the Working Set requires to operate correctly, default: 0 |
| NumberOfSection | minimum required number of sections that the Working Set requires to operate correctly, default: 0 |
| NumberOfControlChannels | minimum required number of individual control channels that the Working Set requires to operate correctly, default: 0 |
| Value | Description |
| RequestForLatestStructureLabel | 1: bytes 2..8 of the Request Structure Label message are transmitted as FF. It is used to determine the version of the latest device description structure present at the Task Controller or Data Logger. 0 :default |
| paramValue | new value for the parameter |
| simulNode | Simulation node to apply the function. |

## Example

```c
if (Iso11783IL_PDDSetParameter( "debug", 1 ) == 0) {
  write( "Debug mode activated" );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1 9.0: form 2 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
