# linGetProtectedID

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linGetProtectedID (long frameID)
```

## Description

With this function it is possible to calculate protected ID for the corresponding LIN frame identifier (i.e. the frame identifier with parity bits).

## Return Values

Returns the calculated protected identifier or a value greater than 255 on failure.

## Example

Display in Write Window a protected ID for each LIN frame seen on the bus

```c
on linFrame *
{
dword pid;
pid = linGetProtectedID(this.ID);
writeLineEx(0,0, "Protected ID for LIN frame identifier 0x%x is 0x%x", this.ID, pid);
```

## Availability

| Since Version |
|---|
