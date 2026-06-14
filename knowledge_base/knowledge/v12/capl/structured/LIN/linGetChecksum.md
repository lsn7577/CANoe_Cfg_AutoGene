# linGetChecksum

> Category: `LIN` | Type: `function`

## Syntax

```c
byte linGetChecksum(linFrame linFrame)
```

## Description

Returns the checksum of a LIN frame or LIN checksum error.

Checksum model (classic/enhanced) is determined automatically.

## Return Values

Calculated checksum

## Example

Get the checksum of a received LIN frame with name myframe

```c
on linFrame myframe
{
byte checksum;
checksum = linGetChecksum(this);
}
or
// Calculate the checksum of a LIN frame object 
...
byte checksum;
// create a LIN frame object
linFrame 0x1 myLinFrame = { dlc = 1, byte(0) = 1 };
// calculate its checksum
checksum = linGetChecksum(myLinFrame);
```

## Availability

| Since Version |
|---|
