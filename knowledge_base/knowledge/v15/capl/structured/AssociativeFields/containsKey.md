# containsKey

> Category: `AssociativeFields` | Type: `method`

## Syntax

```c
dword map[char[]]::containsKey(char key[]);
dword map[float]::containsKey(float key);
dword map[int64]::containsKey(int64 key):
dword map[long]::containsKey(long key);
```

## Description

Returns the information if a key is available in the field.

## Parameters

| Name | Description |
|---|---|
| key | Key that should be checked. |

## Example

```c
if (m.containsKey(3)) { // ...
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.0 SP5 | 7.0 SP5 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | ✔ | N/A |
