# vtsSetBackplaneRelay

> Category: `VTSystem` | Type: `function`

## Syntax

```c
DWORD vtsSetBackplaneRelay(DWORD bpIndex, DWORD closed);
```

## Parameters

| Name | Description |
|---|---|
| bpIndex | zero based index of the backplane to switch the relay on. |
| closed | 0 opens the relay, 1 closes the relay |

## Example

```c
// Close the relay on the first backplane
vtsSetBackplaneRelay(0, 1);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | 14 | — | — | 5.0 SP2 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
