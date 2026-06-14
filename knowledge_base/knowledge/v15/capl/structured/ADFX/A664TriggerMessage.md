# A664TriggerMessage

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664TriggerMessage (a664Message aMessage, dword mode)
```

## Description

This function triggers the scheduling of the a664Message "aMessage". The message is either scheduled once or periodically. To forward an AFDX message in the analysis branch, use the function output().

## Parameters

| Name | Description |
|---|---|
| aMessage | The message object to be scheduled. |
| Mode | Triggering mode. 0: Immediate (transmit once without considering BAG) 1: SingleShot (transmit once according to BAG) 2: StartCyclic (start cyclic transmission according to the selector value TxCycle) 3: StopCyclic (stop cyclic transmission) |

## Example

```c
// define messages from database
a664Message DEMOMSG_INT1 msgInt1 = {msgChannel = 1};
a664Message DEMOMSG_ALLTYPES myMsg = {msgChannel = 1};

a664TriggerMessage(msgInt1, 0);	// send DEMOMSG_INT1 immediately
a664TriggerMessage(msgInt1, 1);	// send DEMOMSG_INT1 once respecting the BAG
a664TriggerMessage(msgInt1, 2);	// send DEMOMSG_INT1 periodically

myMsg.TxCycle = 100;	// change period from DBC to 100msec
a664InitPayload (myMsg); // set payload to last known signal values myMsg.VFG_OIL_TEMP_AB_32 = 33;  // overwrite signal value within the message
myMsg.FS_FDS_1_HSMU_DEMO_ALLTYPES = 3;  // set FS within the message
a664TriggerMessage(myMsg, 2);	// send cyclic with 100msec period
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
