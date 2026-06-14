# linSetGlobalInterByteSpace

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetGlobalInterByteSpace(dword sixteenthBits);
```

## Description

With this function it is possible to change the inter-byte space for all frame responses. Inter-byte space is the period between the end of the stop bit of the preceding byte and the start bit of the following byte.

By default the inter-byte space is 0.

## Parameters

| Name | Description |
|---|---|
| sixteenthBits | Length of the inter-byte space to set [in units of 1/16th of bit time]. Value range: 0..65535. This corresponds to 0..4095.93 bit times. For a LIN standard compliance: The maximum space between the bytes cannot exceed 40% duration compared to nominal transmission time. |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 's'
{
if ( linSetGlobalInterByteSpace(16) != 0)
{
// from now on the inter-byte space in all frame 
 responses is 1 bit time 
...
}
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
