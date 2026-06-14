# linGetResponseData

> Category: `LIN` | Type: `function`

## Syntax

```c
dword LinGetResponseData(linFrame frameObject);
```

## Description

Queries LIN frame response data for specified FrameId on certain LIN channel.

The FrameId and desired LIN channel number are expected to be set in the LIN frameprior to calling this function.

The frame length, dataybte and checksum byte values will be copied into corresponding fields of LIN frame object.

Note, that in the case there is no response data for the specified FrameId no data is copied.

## Parameters

| Name | Description |
|---|---|
| frameObject | The data structure to be filled in. Note, that the following selectors have to be set prior to calling this function: ID MsgChannel |

## Return Values

Non-zero on success.
Zero on failure or when there is no response data defined.
The non-zero value in real mode is the initial and in simulated mode the actual response counter value.

## Example

```c
on key 'a'
{
   linFrame 0x1 testMsg;
   testMsg.MsgChannel = 1;
   testMsg.ID = 0;
   if (LINGetResponseData(testMsg) > 0)
   {
      writelineex(1,1,"FrameId=%d Length=%d, 0x%X 0x%X 0x%X 0x%X 0x%X 0x%X 0x%X 0x%X;", testMsg.ID,           testMsg.DLC,
      testMsg.byte(0), testMsg.byte(1), testMsg.byte(2), testMsg.byte(3), testMsg.byte(4), testMsg.byte(5), testMsg.byte(6), testMsg.byte(7));
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 SP2 | 7.2 SP2 | 13.0 | 13.0 | — | 1.0 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
