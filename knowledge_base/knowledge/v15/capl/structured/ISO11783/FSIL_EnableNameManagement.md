# FSIL_EnableNameManagement

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword FSIL_EnableNameManagement(dword enable ); // form 1
dword FSIL_EnableNameManagement(dword enable, dword bitMask ); // form 2
dword FSIL_EnableNameManagement(dbNode fs, dword enable); // form 3
dword FSIL_EnableNameManagement(dbNode fs, dword enable, dword bitMask); // form 4
```

## Description

Activates the name management of a node. Not until the name management is activated another node can change the device name of this node by sending a name management message.

## Parameters

| Name | Description |
|---|---|
| fs | FS simulation node to apply the function |
| enable | 1: activate the name management 0: deactivates the name management |
| bitmask | Parts of the device name that are allowed to be changed: bit 0 (LSB): Arbitrary Address Capable bit 1: Industry Group bit 2: System Instance bit 3: System bit 4: Function bit 5: Function Instance bit 6: ECU Instance bit 7 (MSB): Manufacturer Code |

## Return Values

0 on success or IL Error Code

## Example

Example form 2

```c
//allow every component to be changed except arbitrary address capable flag
FSIL_EnableNameManagement(1, 0xFE);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
