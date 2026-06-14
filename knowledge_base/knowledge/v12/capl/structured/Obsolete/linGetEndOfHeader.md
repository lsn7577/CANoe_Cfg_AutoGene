# linGetEndOfHeader

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword linGetEndOfHeader(linFrame busEvent)
```

## Description

This function can be used to retrieve a time stamp of the header part for a certain LIN bus event. The resulting time stamp is a time elapsed since measurement start [in units of 10 µsec].

The time returned by this function corresponds to the end of the Protected ID field as detected by an UART. For the XL-hardware, this includes 9/16 of the stop bit. To calculate the theoretical end of Protected ID field including the stop bit, 7/16 of a bit time should be added. Similarly to calculate the start of the Protected ID field, 9 and 9/16 bit times should be subtracted.

## Return Values

Returns the retrieved time stamp [in units of 10 µsec] or 0 on failure.

## Example

Retrieve time stamps of header (ID byte) on analyzing a receive error event

```c
on linReceiveError
{
long byteIndex; 
dword endHeaderTime;
endHeaderTime = linGetEndOfHeader(this);
...
}
```

## Availability

| Since Version |
|---|
