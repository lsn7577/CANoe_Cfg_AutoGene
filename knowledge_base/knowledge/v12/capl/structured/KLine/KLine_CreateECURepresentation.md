# KLine_CreateECURepresentation

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_CreateECURepresentation(dword channel)
```

## Description

Initialize K-Line ECU communication on given channel.

Must be called in on preStart handler.

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
on preStart
{
   long klineHandle;
   long channelNo;

   channelNo = DiagGetCommParameter( "CANoe.ChannelNumber");
   klineHandle = KLine_CreateECURepresentation( channelNo);
   write( "KLine_CreateECURepresentation at K-Line%d returns %d", channelNo, klineHandle);
}
```

## Availability

| Since Version |
|---|
