# TCIL_ControlStop

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ControlStop(); // form 1
long TCIL_ControlStop( dword option ); // form 2
long TCIL_ControlStop( dbNode tc); // form 3
long TCIL_ControlStop( dbNode tc, dword option ); // form 4
```

## Description

Deactivates the Task Controller and stops sending cyclic messages. A Cannot Claim Address message is sent, if the NMT is activated and the message is not suppressed with the parameter option set to 1.

Removes all device descriptor object pools (DDOPs) too.

## Parameters

| Name | Description |
|---|---|
| tc | TC simulation node to apply the function |
| option | Options1: Suppress sending Cannot Claim Address message |

## Example

Example form 4

```c
void SetDataMaskSize(dword newSize)
{
  // data mask size can only be changed if TC is stopped
  TCIL_ControlStop(TC, 1);
  // wait until Working Sets have detected that TC is offline
  TestWaitForTimeout(3500);
  // change size and restart TC
  TCIL_SetNodeProperty(TC,"dataMaskSize", newSize);
  TCIL_ControlStart(TC);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
