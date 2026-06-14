# frUpdatePDU

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frUpdatePDU(<PDU var>, dword flags, int updateCounter);
```

## Description

This function updates the PDU payload in the assigned FlexRay frames.

The update bit can also be set.

## Parameters

| Name | Description |
|---|---|
| <PDU var> | Name of the variable referenced by the PDU object. The variable name was defined via frPDU when the object was created. |
| Bit Mask | Meaning |
| 0x01 | Update bit is set on transmission. |
| All other bits are reserved and must be set to a value of 0. |  |
| Value | Meaning |
| -1 | The PDU is transmitted in every configured slot. |
| 0 | The PDU's default value is transmitted. |
| N (>0) | The PDU is transmitted at least n times. |

## Return Values

—

## Example

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.1 | 6.1 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
