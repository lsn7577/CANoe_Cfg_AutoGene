# _KLine_FastInitPatternReceived

> Category: `KLine` | Type: `function`

## Syntax

```c
_KLine_FastInitPatternReceived(dword TiniL_us, dword TWup_us, int64 timestampTWup)
```

## Description

Called when a fast init pattern has been received.

Called for the following values:

## Return Values

—

## Example

```c
_KLine_FastInitPatternReceived( dword TiniL_us, dword Twup_us, int64 timestampTwup)
{
   write(FastInitPattern @%.3f received, type %d, TiniL = %d us, Twup = %d us", timestampTwup / cNs2s, type, TiniL_us, Twup_us);
}
```

## Availability

| Since Version |
|---|
