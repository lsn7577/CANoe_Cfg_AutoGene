# _KLine_FrameTransmissionCon

> Category: `KLine` | Type: `function`

## Syntax

```c
_KLine_FrameTransmisionCon(BYTE data[], int64 timestamps[])
```

## Description

Is called when a frame has been transmitted.

## Return Values

—

## Example

```c
_KLine_FrameTransmissionCon(BYTE data[], int64 timestamps[])
{
   int i;
   int64 p4Time;
   dword systemBaudRate;
   int64 byteLength_ns;
   systemBaudRate  = 10400;
   byteLength_ns = ((1.0/systemBaudRate) * 10) * 1000000000; // 10 bit times in ns

   // Calculate P4 Times
   for (i = 0; i < elcount(data)-1; ++i)
   {
      p4Time = (timestamps[i+1] - byteLength_ns) - timestamps[i];
      write("P4 time between byte no.: %d; Value: %x and byte no.: %d; Value: %x == [%.6f s]\n ", i,    data[i], i+1, data[i+1], p4Time/1000000000.0);
   }
}
```

## Availability

| Since Version |
|---|
