# linSetChecksumCompatibility

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetChecksumCompatibility(long channel)
```

## Description

Switches the checksum calculation model of all frames that have at least one subscribed LIN 1.x node to the classic model.

This function may only be called in the event procedure on preStart.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on prestart
{
  /*send and receive all frames that are received by at least one Lin 1.x node using the classic checksum model.*/
  linSetChecksumCompatibility();
}
on prestart
{
  /*send and receive all frames on channel 1 that are received by at least one Lin 1.x node using the classic checksum model.*/
  linSetChecksumCompatibility(1);
}
```

## Availability

| Since Version |
|---|
