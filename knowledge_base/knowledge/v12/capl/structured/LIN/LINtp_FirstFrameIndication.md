# LINtp_FirstFrameIndication

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_FirstFrameIndication(long sender, long receiver, long announcedLen);
```

## Description

Indicates the start of a segmented reception.

## Return Values

—

## Example

```c
LINtp_FirstFrameIndication(long sender, long receiver, long announcedLen)
{
  write( "Start reception of %d bytes", announcedLen);
}
```

## Availability

| Since Version |
|---|
