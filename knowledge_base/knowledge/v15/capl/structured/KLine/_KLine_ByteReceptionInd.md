# _KLine_ByteReceptionInd

> Category: `KLine` | Type: `function`

## Syntax

```c
_KLine_ByteReceptionInd(BYTE byteIn, int64 endOfByteTimes_ns)
```

## Description

Is called when a byte has been received.

## Parameters

| Name | Description |
|---|---|
| byteIn | Received byte |
| endOfByteTimes_ns | End of byte time stamp in ns resolution. |

## Return Values

—

## Example

```c
_KLine_ByteReceptionInd(BYTE byteIn, int64 endOfByteTimes_ns)
{
   int64 endOfByteCorrection_ns;
   dword systemBaudRate;
   float uartSamplePoint;
   systemBaudRate  = 10400;
   uartSamplePoint = 0.5;
   write("Byte Value: %x", byteIn);
   write("End of Byte Time: [%.9f]", endOfByteTimes_ns/1000000000.0);
   // UART sample point corrected end of byte time. UART samples in the middle of a bit.
   endOfByteCorrection_ns = ((1.0/systemBaudRate) * uartSamplePoint) * 1000000000;
   write("Corrected End of Byte Time: [%.9f]", (endOfByteTimes_ns + endOfByteCorrection_ns)/1000000000.0);
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
