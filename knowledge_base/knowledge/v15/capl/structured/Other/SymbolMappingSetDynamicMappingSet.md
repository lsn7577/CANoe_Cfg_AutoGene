# SymbolMappingSetDynamicMappingSet

> Category: `Other` | Type: `function`

## Syntax

```c
void SymbolMappingSetDynamicMappingSet(char mappingSetName[]);
```

## Description

Changes the dynamic mapping set that will be used for mapping in the CANoeSymbol Mapping dialog. Only the mapping relations contained in the given dynamic mapping set and in the static mapping set are considered.

## Parameters

| Name | Description |
|---|---|
| mappingSetName | Name of a dynamic set which shall be activated. |

## Example

```c
on key '1'
{
  // Activate DataSet1 and map its contained mapping relations
  SymbolMappingSetDynamicMappingSet ("DataSet1");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 11.0 SP3 | 11.0 SP3 | 13.0 | — | 14 | 3.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
