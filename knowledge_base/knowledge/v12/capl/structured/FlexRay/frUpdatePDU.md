# frUpdatePDU

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frUpdatePDU(<PDU var>, dword flags, int updateCounter);
```

## Description

This function updates the PDU payload in the assigned FlexRay frames.

The update bit can also be set.

## Return Values

—

## Example

Example

The following example assumes that the database defines a PDU that is named PDU_CNT_02 and that this PDU contains a signal that is named counter.

This program sends the PDU once every 64 cycles. The update is made on the beginning of cycle 0.

```c
variables
{
   frPDU MsgChannel%CHANNEL%.PDU_CNT_02 gPDU1;
   BYTE gCycle; // remember current FlexRay cycle
}
on preStart
{
   // Optionally prepare buffer for PDU gPDU1:
   frSetSendPDU(gPDU1);
}
on frStartCycle 0
{
   if (this.MsgChannel != %CHANNEL%) return;
   gCycle = this.FR_Cycle;
   gPDU1.counter = gCycle;
   frUpdatePDU(gPDU1, 1, 1); // set update bit and send only once
}
```

## Availability

| Since Version |
|---|
