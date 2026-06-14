# linSetInterframeSpace

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetInterframeSpace(dword bitTimes);
```

## Description

This function sets the minimum inter-frame space.

With this function it is possible to change the inter-frame space for all frames.

The inter-frame space is the time from the end of the frame until start of the next frame.

By default the minimum inter-frame space is 0.

## Parameters

| Name | Description |
|---|---|
| bitTimes | Length of the inter-frame space to set [in bit times].Value range: 0..255 |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 's'
{
if (linSetInterframeSpace (200) != 0)
{
// from now on inter-frame space is minimum 200 bit times 
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
