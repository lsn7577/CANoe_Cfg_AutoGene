# _KLine_FrameReceptionInd

> Category: `KLine` | Type: `function`

## Syntax

```c
_KLine_FrameReceptionInd(BYTE data[], int64 timestamps[])
```

## Description

Is called when a frame has been received.

## Parameters

| Name | Description |
|---|---|
| data | Received data buffer of the frame. |
| timestamps | End of byte time stamps of the received data bytes. |

## Return Values

—

## Example

```c
_KLine_FrameReceptionInd(BYTE data[], int64 timestamps[])
{
   int i;
   int64 p1Time;
   dword systemBaudRate;
   int64 byteLength_ns;
   systemBaudRate  = 10400;
   byteLength_ns = ((1.0/systemBaudRate) * 10) * 1000000000; // 10 bit times in ns
   // Calculate P1 Times
   for (i = 0; i < elcount(data)-1; ++i)
   {
      p1Time = (timestamps[i+1] - byteLength_ns) - timestamps[i];
      write("P1 time between byte no.: %d; Value: %x and byte no.: %d; Value: %x == [%.6f]\n ", i, data[i], i+1,    data[i+1], 
      1Time/1000000000.0);
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.0 | 8.0 | — | — | — | 1.1 SP2 |
| Restricted To | K-Line Real bus mode ECU tester | K-Line Real bus mode ECU simulation ECU tester | — | — | — | K-Line Real bus mode ECU simulation ECU tester |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
