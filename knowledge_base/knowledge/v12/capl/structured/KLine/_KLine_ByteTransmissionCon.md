# _KLine_ByteTransmissionCon

> Category: `KLine` | Type: `function`

## Syntax

```c
_KLine_ByteTransmissionCon(BYTE byteIn, int64 endOfByteTimes_ns)
```

## Description

Is called when a byte has been transmitted.

## Return Values

—

## Example

```c
_KLine_ByteTransmissionCon(BYTE byteIn, int64 endOfByteTimes_ns)
{  int64 endOfByteCorrection_ns;
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

| Since Version |
|---|
