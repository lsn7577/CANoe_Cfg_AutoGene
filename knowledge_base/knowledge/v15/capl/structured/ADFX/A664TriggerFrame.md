# A664TriggerFrame

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664TriggerFrame (a664Frame aFrame, dword mode)
```

## Description

This function triggers the transmission of a single a664Frame "aFrame" either immediately or respecting the BAG. To forward an AFDX frame in the analysis branch, use the function output().

## Parameters

| Name | Description |
|---|---|
| aFrame | The frame object to be scheduled. |
| mode | Triggering mode. 0: Immediate (transmit once without considering BAG) 1: SingleShot (transmit once according to BAG) |

## Example

```c
a664Message DEMOMSG_ALLTYPES myMsg = {msgChannel = 1};
a664Frame * myFrame;
myMsg.TxCycle = 100;
myMsg.VFG_OIL_TEMP_AB_32 = 33;
myMsg.FS_FDS_1_HSMU_DEMO_ALLTYPES = 3;

// use myMsg as source to define a frame for manipulations
myFrame = myMsg;
myFrame.UdpDstPort = 3333;	// change UDP destination port
a664TriggerFrame(myFrame, 1);  // transmit the frame respecting the BAG
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP3 | 9.0 SP3 | — | — | — | — |
| Restricted To | AFDX | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
