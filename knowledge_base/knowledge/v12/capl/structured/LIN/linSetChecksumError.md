# linSetChecksumError

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetChecksumError(long frameId, long activate)
```

## Description

Sets/resets a checksum error of a LIN frame. The activated checksum error is then constant and will not be affected by changes in the frame data.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

Cause check sum error for all LIN frames on the bus

```c
on linFrame *
{
linSetChecksumError(this.id, 1);
}
```

## Availability

| Since Version |
|---|
