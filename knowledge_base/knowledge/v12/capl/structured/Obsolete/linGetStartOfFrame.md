# linGetStartOfFrame

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword linGetStartOfFrame(linFrame busEvent)
```

## Description

This function can be used to retrieve a start time stamp of a LIN bus event. The resulting time stamp is a time elapsed since the measurement start [in units of 10 µsec].

## Return Values

Returns the retrieved time stamp [in units of 10 µsec] or 0 on failure.

## Example

Calculate header length [in bit times] for each received LIN frame

```c
on linFrame *
{
dword startOfFrame, endOfHeader, headerLength;
if (this.dir != RX)
{
return; // ignore transmitted frames
}
startOfFrame = linGetStartOfFrame(this); // retrieve frame start time 
endOfHeader = linGetEndOfHeader(this); // retrieve header end time
headerLength = linTime2Bits(endOfHeader - startOfFrame); // calculate header length in bit times
// display the result in Write window
writeLineEx(0,0, "Header length for LIN frame 
 with identifier 0x%x is %d bit times", this.ID, headerLength);
}
```

## Availability

| Since Version |
|---|
