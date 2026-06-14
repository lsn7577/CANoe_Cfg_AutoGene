# mostSetTimingMode

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetTimingMode(long channel, long mode)
```

## Description

This function configures the MOST hardware as a Timing Master (mode = 1) or Timing Slave (mode = 0).

MOST25: For further information on Master/Slave switchover functionality see also the description of the MTR bit in the Transceiver Control Register of the OS8104.

MOST50/150: Switching from Slave to non-static Master does not wake the network automatically. Use mostWakeup to start the network.

If the bypass is closed (see mostSetAllBypass()) this function has no effect until the bypass is opened.

## Return Values

See error codes

## Availability

| Since Version |
|---|
