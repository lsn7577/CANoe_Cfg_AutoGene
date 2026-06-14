# MessageTimeNS

> Category: `Other` | Type: `function`

## Syntax

```c
float MessageTimeNS(message msg);
```

## Description

Returns the time stamp in nanoseconds.

The time stamp that can be polled with this function has a greater precision than the msg.TIME time stamp, whereby the precision depends on the CAN or LIN hardware that is being used.

## Return Values

Time stamp of the message in ns

## Availability

| Since Version |
|---|
