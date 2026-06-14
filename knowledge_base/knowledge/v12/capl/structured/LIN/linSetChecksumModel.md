# linSetChecksumModel

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetChecksumModel(long channel, long frameID, long checksumModel)
```

## Description

Sets the checksum calculation model of a single frame.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on prestart
{
  /*send and receive the frame with the ID “4” using the classic checksum model*/
  linSetChecksumModel(4,0);
}
on prestart
{
  /*send and receive the frame with the ID “4” on channel 1 using the classic checksum model*/
  linSetChecksumModel(1,4,0);
}
```

## Availability

| Since Version |
|---|
