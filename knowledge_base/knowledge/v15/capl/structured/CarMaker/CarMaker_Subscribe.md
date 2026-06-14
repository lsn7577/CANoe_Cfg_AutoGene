# CarMaker_Subscribe

> Category: `CarMaker` | Type: `function`

## Syntax

```c
long CarMaker_Subscribe(char group[], double freq_hz);
```

## Description

Subscribes a group of CarMaker quantities as CANoe system variables. The CANoe system variables are defined in the CarMaker system variable namespace. Each call to this function automatically unsubscribes any previous subscription.

## Parameters

| Name | Description |
|---|---|
| group | Name of the group of quantities to subscribe. |
| freq_hz | The frequency at which the values are to be sent. The reception is then processed inside the polling function. |

## Return Values

APO return code

## Example

```c
// subscribe to quantities of CarMaker
gErrorState = CarMaker_Subscribe("TC1_Group", gFreq_Hz);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | CarMaker | — | — | — | CarMaker |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
