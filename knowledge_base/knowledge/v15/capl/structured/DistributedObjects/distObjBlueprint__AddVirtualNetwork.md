# distObjBlueprint::AddVirtualNetwork

> Category: `DistributedObjects` | Type: `method`

## Syntax

```c
void distObjBlueprint *::AddVirtualNetwork(char networkPath[]);
void distObjBlueprint *::AddVirtualNetwork(virtNet network);
```

## Description

Adds a virtual network to the blueprint.

## Parameters

| Name | Description |
|---|---|
| networkPath | Fully qualified name of the virtual network to add. |
| network | Virtual network to add. |

## Return Values

—

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  interface SomeInterface {}
  virtualNetwork SomeNetwork;
}

// CAPL
on key 'a' {
  distObjBlueprint SomeInterface bp;
  bp = SomeInterface.CreateObjectBlueprint();
  bp.AddVirtualNetwork("SomeNamespace::SomeNetwork");
  bp.AddVirtualNetwork(SomeNetwork);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | 14 | 15 | 14 | 5.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
