# linMrSchedSetRqId

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void linMrSchedSetRqId (unsigned int requestId, unsigned long period, unsigned char modeFlags[]);
```

## Description

Creates an entry for the Scheduler.

linMrSchedSetRqId may only be called once for each LIN Message Identifier. During a processing step of the Scheduler the outstanding transmit requests are serviced in the order in which they were configured by linMrSchedSetRqId.

## Return Values

—

## Availability

| Up to Version |
|---|
