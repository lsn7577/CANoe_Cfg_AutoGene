# mostAmsOutput

> Category: `MOST` | Type: `function`

## Syntax

```c
mostAmsOutput(long channel, long destAdr, char symbolicMessage[], long instId)
```

## Description

Definition and direct dispatch of an AMS message using the syntax from the MOST specification and the description in the XML function catalog.

The description of the message must be complete, i.e. wildcards cannot be used because the message should then be sent directly. However, the parameter list may be shorter than specified in the function catalog, in order to be able to generate intentionally incomplete messages.

## Return Values

—

## Example

```c
// send 'play' command 
 for DiskPlayer on MOST ring
on key 'p'
{
   // Send command on channel 1 to instanceId 1 of functionblock "AudioDiskPlayer"
   mostAmsOutput(1,"AudioDiskPlayer.SourceActivity.StartResult(1,On)",1);
}
```

## Availability

| Since Version |
|---|
