# coTfsLifeGuarding

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLifeGuarding( dword guardTime, dword retryFactor, dword tolerance );
```

## Description

The test sets the guard time and retry factor objects in the DUT Device Under Test. After that, 20 guarding remote frames are sent to the target device which must respond to all queries within the guardTime+tolerance.

Afterwards the sending of the remote frames is stopped. It is waited for the corresponding emergency message (EMCY code = 0x8130, Error Register = 0x11) before the values of the guard time and retry factor objects are reset.

## Parameters

| Name | Description |
|---|---|
| guardTime | Guard time in milliseconds. |
| retryFactor | Retry factor |
| tolerance | Permitted time deviation of the target device in milliseconds. It is recommended that you use an even value. The tolerated time frame within which a message is still accepted is: x - (delta/2) <= x <= x + (delta/2) |

## Return Values

Error code

## Example

```c
if ( coTfsLifeGuarding ( 500, 5, 50) != 1) {  // guard time, retry Factor, tolerance
  write("lifeguarding failed");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
