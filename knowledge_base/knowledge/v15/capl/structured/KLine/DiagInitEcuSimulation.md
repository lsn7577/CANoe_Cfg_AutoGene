# DiagInitEcuSimulation

> Category: `KLine` | Type: `function`

## Syntax

```c
long DiagInitEcuSimulation(char ecuQualifier[])
```

## Description

Initialize CAPL node to represent a diagnostics ECU simulation. From now on the ECU can interpret and use all diagnostic objects in the CAPL code of this node as defined by the respective diagnostic description.

CANoe will initialize the CAPL callback interface for diagnostics during the call.

## Parameters

| Name | Description |
|---|---|
| ecuQualifier | Qualifier of the ECU as set in the diagnostic configuration dialog for the respective diagnostic description. |

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
on preStart
{
   char ecuQual[10] = "KLineECU";
   write( "DiagInitEcuSimulation( %s): %d", ecuQual, DiagInitEcuSimulation(ecuQual));
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 SP4 | — | — | — | 1.1 SP2 |
| Restricted To | — | Real bus mode Online mode ECU simulation | — | — | — | Real bus mode Online mode ECU simulation |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
