# lookupVirtNet

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
virtNet lookupVirtNet(char path[]);
```

## Description

Obtains a virtual network by using a string.

## Parameters

| Name | Description |
|---|---|
| path | Fully qualified name of the virtual network. |

## Return Values

Virtual network with the given path.
Invalid virtual network if nothing was found.

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  virtualnetwork VN;
}

// CAPL
on key 'a' {
  DoSomething(lookupVirtNet("SomeNamespace::VN"));
}

void DoSomething(virtNet p) {}
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
