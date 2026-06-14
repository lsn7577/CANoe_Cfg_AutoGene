# A664TriggerFrame

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664TriggerFrame (a664Frame aFrame, dword mode)
```

## Description

This function triggers the transmission of a single a664Frame "aFrame" either immediately or respecting the BAG. To forward an AFDX frame in the analysis branch, use the function output().

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

| Since Version |
|---|
