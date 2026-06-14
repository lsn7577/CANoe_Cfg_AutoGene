# A664TriggerMessage

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664TriggerMessage (a664Message aMessage, dword mode)
```

## Description

This function triggers the scheduling of the a664Message "aMessage". The message is either scheduled once or periodically. To forward an AFDX message in the analysis branch, use the function output().

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

| Since Version |
|---|
