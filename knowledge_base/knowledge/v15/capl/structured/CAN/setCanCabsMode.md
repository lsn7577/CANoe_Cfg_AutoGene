# setCanCabsMode

> Category: `CAN` | Type: `function`

## Syntax

```c
long setCanCabsMode(long ntype,long nchannel,long nmode,long nflags);
```

## Description

Various CANcabs modes may be set. Replaces the setPortBits functions.

## Parameters

| Name | Type | Description |
|---|---|---|
| ntype |  | Unused, must be set to 0 |
| nchannel |  | CAN channel |
| 0 |  | NORMAL |
| 1 |  | SLEEP |
| 2 |  | HIVOLTAGE |
| 3 |  | HISPEED |
| 4 |  | DUAL_WIRE |
| 5 |  | SINGLE_WIRE_LOW |
| 6 |  | SINGLE_WIRE_HIGH |
| 7 |  | is reserved |
| nMode | Line 2 | Line 1 |
| 8 | 0 | 0 |
| 9 | 0 | 1 |
| 10 | 1 | 0 |
| 11 | 1 | 1 |
| Example Call the function with ntype = 0, nchannel = 1, nMode = 11, nflags = 0 setCanCabsMode(0,1,11,0); // sets both lines to 1 |  |  |
| 0x0 |  | HIGHPRIO is disabled |
| 0x1 |  | HIGHPRIO is enabled (clear tx-buffers) |
| 0x4 |  | HIGPRIO is enabled for one message (clear tx-buffers) |
| Note Not all mode and flag values are valid for all CANcabs! (see also the hardware description for CANcabs) |  |  |

## Example

```c
on key 'n'
{
   long ntype, nmode, nchannel, nflags;
   ntype = 0;
   nmode = 0;
   nchannel = 1;
   nflags = 0;
   setCanCabsMode(ntype, nchannel, nmode, nflags);
   write("normal mode");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 4.1 | 4.1 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
