# _KLine_FrameReceptionInd

> Category: `KLine` | Type: `function`

## Syntax

```c
_KLine_FrameReceptionInd(BYTE data[], int64 timestamps[])
```

## Description

Is called when a frame has been received.

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

| Since Version |
|---|
