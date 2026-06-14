# linGetSyncDelLength

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword linGetSyncDelLength(linFrame busEvent)
```

## Description

This function can be used to retrieve the synch delimiter (recessive bits) length of a LIN bus event. The resulting length is in units of 10 µsec (microseconds).To get the result in bit times linTime2Bits() function can be used.

## Return Values

Returns the retrieved length [in units of 10 µsec] or 0 on failure.

## Example

Analyze receive error event by retrieving length of synch break and sync delimiter

```c
on linReceiveError
{
dword timelenBreak,timelenDel;
dword bitlenBreak,bitlenDel;
timelenBreak = linGetSyncBreakLength(this); // retrieve 
 break length in time units
bitlenBreak  = linTime2Bits(timelenBreak);  // convert time units to bit times
timelenDel   = linGetSyncDelLength(this);   // retrieve delimiter length in time units
bitlenDel    = linTime2Bits(timelenDel);    // convert time units to bit times
...
}
```

## Availability

| Since Version |
|---|
