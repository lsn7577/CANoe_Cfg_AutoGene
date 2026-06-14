# canSetChannelAcc

> Category: `CAN` | Type: `function`

## Syntax

```c
long canSetChannelAcc(long channel, dword code, dword mask);
```

## Description

Via an acceptance filter the CAN controllers control which received messages are sent through to CANoe.Some controller chips, such as the SJA 1000, expect partitioning into acceptance mask and acceptance code.

## Return Values

0: ok

## Example

```c
on key 'a'
{
/*
To distinguish whether the filter is for standard or extended identifier. For extended identifiers the MSB of the code and mask are set.
Description:
Different ports may have different filters for a channel. If the CAN hardware cannot implement the filter, the driver virtualises filtering.
Accept if ((id ^ code) & mask) == 0). 
*/
   long channel =2;
   dword code=0x10;
   dword mask=0x10;
   canSetChannelAcc(channel,code,mask);
   write("channel mask set");
}
```

## Availability

| Since Version |
|---|
