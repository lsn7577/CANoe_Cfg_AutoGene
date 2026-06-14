# linSetBaudrate

> Category: `LIN` | Type: `function`

## Syntax

```c
void linSetBaudrate(long baudrate)
```

## Description

With this function it is possible to change the baud rate during the measurement.

It is also possible to activate automatic baud rate detection in a specified range.

## Return Values

—

## Example

Change baud rate on keyboard event

```c
on key 'w'
{
linSetBaudrate(9600);  // change baudrate to 9600 bit/sec
}
```

## Availability

| Since Version |
|---|
