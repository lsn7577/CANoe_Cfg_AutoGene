# frFrame

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frFrame <frame name> <frame var>; // form 1
frFrame MsgChannel<num>.<frame name> <frame var>; // form 2
frFrame (<slot ID>, <base cycle>, <cycle repetition>) <frame var>; // form 3
frFrame MsgChannel<num>.(<slot ID>, <base cycle>, <cycle repetition>) <frame var>; // form 4
```

## Description

Can be used to create a FlexRay send object. The object data can be manipulated by selectors associated with this object. Other object characteristics can be read out from selectors.

Objects are then registered using the frSetSendFrame and are sent using the frUpdateStatFrame or frOutputDynFrame functions.

## Parameters

| Name | Description |
|---|---|
| MsgChannel<num> | Defines the send channel/cluster. <num> must be an integer (e.g. 1, 2, 3, etc.) defining the channel number of the corresponding FlexRay interface. |
| <frame name> | Character string corresponding to a frame name from the database. The required parameters (<slot ID>, <base cycle>, <cycle repetition> and <channel mask>) are taken from the corresponding frame definition in the database. |
| <frame var> | Character string defining the object’s variable name. |
| <slot ID> | This number designates a specific slot. Its value must be between 1 and 2047. |
| <base cycle> | This number designates the base cycle. This value must be smaller than the repetition factor and lies in the range between 0 and 63. This value, together with the repetition factor, determines the "Cycle Multiplexing". |
| <cycle repetition> | This number designates the cycle repetition factor. The value must be between 1 and 64 and be a multiple of 2 (e.g. 1, 2, 4, 8, 16, 32 or 64). This value, together with the base cycle, determines the "Cycle Multiplexing". |

## Example

Example 1

For an example see function frUpdateStatFrame.

Example 2

This is an example for forwarding the payload to other functions.

Example 3

This is an example for using the frame object as a function parameter.

Example 4

This is an example for using the Frame object in arrays.

Caution!

All objects of an array must be initialized with an appropriate frame definition!

```c
variables
{
  const dword cFrTTFlag = 0x00;
  const dword cFrETFlag = 0x10;
  const dword cFrPPFlag = 0x20;
  const dword cFrStopFlag = 0x80; // only for VN
  const dword cFrNullFlag = 0x400; // only for VN
}

void foo (byte data[], int bytecount)
{
  // evaluate or set the contents of the data array
}

void example ()
{
  frFrame (1,0,1) myFrame  = { FR_Flags = cFrTTFlag | cFrPPFlag, FR_ChannelMask = 1, FR_PayloadLength = 2 };
  foo (myFrame.FR_Payload, myFrame.FR_PayloadLength * 2);
}
variables
{
  const dword cFrTTFlag = 0x00;
  const dword cFrETFlag = 0x10;
  const dword cFrPPFlag = 0x20;
  const dword cFrStopFlag = 0x80; // only for VN
  const dword cFrNullFlag = 0x400; // only for VN

  frFrame (1,0,1) myFrame  = { FR_Flags = cFrTTFlag | cFrPPFlag, FR_ChannelMask = 1, FR_PayloadLength = 2 };
}

void foo (frFrame * frame)
{
  // evaluate or set the contents of the frame object
}

void example ()
{
  foo (myFrame);
}
variables
{
  frFrame (1,0,1) frm1;

  // All objects are equal:
   frFrame (2,0,1) frArray1[10];

  // All objects may be different:
  frFrame * frArray2[3] = { (3,0,1), <FrameNameFromDB>, frm1 };
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.1 7.5: enhanced for usage in arrays and as function parameter | 6.1 7.5: enhanced for usage in arrays and as function parameter | 13.0 | — | — | 1.0 |
| Restricted To | FlexRay | FlexRay | FlexRay | — | — | FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
