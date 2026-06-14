# output (CAN)

> Category: `CAN` | Type: `function`

## Syntax

```c
void output(message msg); // form 1
void output(errorFrame); // form 2
```

## Description

Outputs a message (form 1) or an Error Frame (form 2) from the program block.

## Parameters

| Name | Description |
|---|---|
| msg | Variable of type message. |
| errorFrame | Variable of type errorFrame. |

## Return Values

—

## Example

output(msg) Example

output(errorFrame) Example

Except for the first channel for all other channels the key word errorFrame has to be qualified with the number of the CAN channel.

```c
variables {
message can2.125 msg = { // define CAN message 
dlc = 1,
byte(0) = 1
};
}
on key F1 {
output (msg); // output Message
}
on key F10 {
output(errorFrame); // output Error Frame on CAN channel 1
}
on CAN2.errorFrame {
output (CAN3.errorFrame); // output Error Frame on CAN channel 3
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | All | All | 13.0 | 13.0 | — | 1.0 |
| Restricted To | CAN | CAN | CAN | CAN | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
