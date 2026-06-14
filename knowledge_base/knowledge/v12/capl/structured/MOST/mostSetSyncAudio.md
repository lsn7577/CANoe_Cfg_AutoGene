# mostSetSyncAudio

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetSyncAudio(long channel, long channels[4], long device, long mode)
```

## Description

The function programs the routing engine for the audio input or output of the bus interface. The functions works independently of whether the synchronous channels are reserved. The user must ensure the reservation, e.g. by sending an Alloc message to the timing master.

MOST50 / MOST150: The function performs the routing of audio input or output of the bus interface. At completion of the routing operation the event procedure OnMostSyncAudio() will be called.

mostSetSyncAudio automatically allocates new channels to which Line-In is routed. (Device==0).

This function is only available if the connected hardware interface has its bypass opened.

## Return Values

See error codes

## Availability

| Since Version |
|---|
