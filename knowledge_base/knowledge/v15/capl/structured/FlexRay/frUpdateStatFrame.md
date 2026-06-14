# frUpdateStatFrame

> Category: `FlexRay` | Type: `function`

## Syntax

```c
int ret = frUpdateStatFrame( <frame var> );
```

## Description

This function updates the FlexRay Communication Controller's (CC) send buffer with the current data from the send object. This corresponds to a request to send.

Only frames in the static segment can be sent using this function!

## Parameters

| Name | Description |
|---|---|
| <frame var> | Name of the variable referenced by the frame object. The variable name was defined when the object was created using frFrame. |

## Example

The following CAPL program sends a start-up/sync frame in slot 60 in every cycle. The calculation of the payload and the Tx buffer update is synchronously executed to every start of a cycle.

```c
variables
{
  // The gMsg1 message is a start-up/sync message for the static segment
  // that is sent on both channels.

  frFrame ( 20, 0, 1) gMsg1;
  const LONG gMsg1Channel  = %CHANNEL%; // send on network the CAPL node is assigned to
  const LONG gMsg1ChanMask = 3;  // send on FlexRay channel A+B
  const long gMsg1KeySlotIndex = 1; // use key slot 1
  const LONG gMsg1KeySlotID = 20; // send in key slot 20 (static segment)
  const LONG gMsg1KeySlotUsg = 3; // sync and startup
  BYTE gMsg1Len; // Payload length
  BYTE gCycle; // remember current FlexRay cycle
  frConfiguration gFRParams;
}

on preStart
{
  // Calculation of Payload length
  frGetConfiguration(%CHANNEL%, gFRParams);
  gMsg1Len = gFRParams.gPayloadLengthStatic * 2;
  // Optionally prepare buffer for message gMsg1:
  gMsg1.MsgChannel = gMsg1Channel;
  gMsg1.FR_ChannelMask = gMsg1ChanMask;
  frSetPayloadLengthInByte(gMsg1, gMsg1Len);
  frSetKeySlot(gMsg1Channel, gMsg1ChanMask, gMsg1KeySlotIndex, gMsg1KeySlotID, gMsg1KeySlotUsg);
}

DoFRCalc ()
{
  int i;
  gMsg1.byte(0) = gCycle;
  // or gMsg1.signame = value; if frame is symbolically declared
  for (i = 1; i < gMsg1.FR_PayloadLength * 2; ++i)
  {
    gMsg1.byte(i) = i;
  }
}

DoFRSend ()
{
  // Update the message buffer:
  frUpdateStatFrame(gMsg1); // or FROutputDynFrame(gMsg1);
}

on frStartCycle *
{
  gCycle = this.FR_Cycle;
  DoFRCalc(); // calculate and set message contents
  DoFRSend(); // commit buffer for sending
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
