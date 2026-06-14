# linGetByteEndTime

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword linGetByteEndTime(linFrame busEvent, long index)
```

## Description

This function can be used to retrieve a data byte time stamp of a certain LIN bus event. The resulting time stamp is a time elapsed since measurement start [in units of 10 µsec].

The time returned by this function corresponds to the end of the data byte field as detected by an UART. For the XL-hardware, this includes 9/16 of the stop bit. To calculate the theoretical end of data byte field including the stop bit, 7/16 of a bit time should be added. Similarly to calculate the start of the data byte field, 9 and 9/16 bit times should be subtracted.

## Return Values

Returns the retrieved time stamp [in units of 10 µsec] or 0 on failure.

## Example

Retrieve time stamps of each data byte on analyzing a receive error event

```c
on linReceiveError
{
long byteIndex;
dword byteTimestamp;
if (0 == this.lin_ShortError)  // 
 .DLC selector only valid when .lin_ShortError is not set
{
for (byteIndex=1; byteIndex <= this.DLC; ++byteIndex) 
 
{
byteTimestamp = linGetByteEndTime(this, byteIndex);
...
}
}
}
```

## Availability

| Since Version |
|---|
