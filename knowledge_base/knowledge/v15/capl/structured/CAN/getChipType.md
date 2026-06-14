# getChipType

> Category: `CAN` | Type: `function`

## Syntax

```c
long getChipType(long channel);
```

## Description

Determines the type of CAN controller used.

## Parameters

| Name | Description |
|---|---|
| 0 | both controller |
| 1 | Channel 1 |
| 2 | Channel 2 |

## Return Values

Type of controller with the following values:
Other types may occur. DEMO versions return the result 0 or simulate one of the existing types. If an attempt is made to access a nonexistent channel (e.g. Channel 2 for CPC/PP) or if the driver used does not support this function, the functional result is 0.

## Example

```c
...
switch(getChipType(0)) {
case 200: setOcr(0,0x02);
break;
case ...
default:
write("Unknown CAN-chip %d", getChipType(0));
break;
}
...
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
