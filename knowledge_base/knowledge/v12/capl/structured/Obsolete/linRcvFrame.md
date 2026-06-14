# linRcvFrame

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void linRcvFrame (long syncTimeStamp, long origTimeStamp, int msgId, int frameDlc, int frameDir, int bytecount, byte data[])
```

## Description

A function defined in CAPL with the exact signature shown above receives all LIN frames that are occurring on the bus and are not filtered out by a global message filter.

## Return Values

—

## Availability

| Up to Version |
|---|
