# mostSetSyncSpdif

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetSyncSpdif(long channel, long channels[8], long device, long mode)
```

## Description

The function programs the routing engine for S/PDIF input or output of the bus interface. The function works independently of whether the synchronous channels are reserved. The user must ensure the reservation, e.g. by sending an Alloc message to the timing master.

MOST50 / MOST150: The function performs the routing of S/PDIF input or output of the bus interface. At completion of the routing operation the event procedure OnMostSyncSpdif() will be called.

mostSetSyncSpdif automatically allocates new channels to which the S/PDIF In is routed. (Device==0).

SPDIF In (device==0) is only available if the connected hardware interface has its bypass opened.

Call mostSetSyncMute to mute/demute the signal.

## Return Values

See error codes

## Availability

| Since Version |
|---|
