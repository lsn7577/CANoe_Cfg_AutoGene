# output (J1939)

> Category: `J1939` | Type: `function`

## Syntax

```c
output(pg pg_variable);
```

## Description

Outputs a parameter group onto the CAN bus.

## Parameters

| Name | Description |
|---|---|
| pg_variable | Variable of the type "pg". |

## Return Values

—

## Example

```c
variables {
pg 0xFEE1 pg_1 = { // Definition of a parameter group
};
}
on key F1 {
output (pg_1); // Output parameter group
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 SP3 | 8.2 SP3 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | J1939 | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
