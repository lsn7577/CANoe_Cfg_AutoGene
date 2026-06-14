# linSetRespCounter

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetRespCounter(long frameID, long count)
```

## Description

With this function it is possible to limit the number of responses sent for the specified frame identifier.

By setting count = 0 it is possible to deactivate the frame response completely.

With count = -1 a frame response is always sent when a correct frame header is received. This is the default configuration for newly configured frames.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| Since Version |
|---|
