# convertTimestamp, convertTimestampNS

> Category: `Other` | Type: `function`

## Syntax

```c
void convertTimestamp(dword timestamp, dword& days, byte& hours, byte& minutes, byte& seconds, word& milliSeconds, word& microSeconds); // form 1
```

## Description

Converts a time stamp to separate parts

(form 1: maximum time: .2^32 * 10 microseconds = 11 hours, 55 minutes, 49 seconds, 672 milliseconds, 96 microseconds).

## Return Values

—

## Example

```c
on envVar EnvGearUp
{
   dword d;
   byte h, m, s;
   word ms, us, ns;
   convertTimestampNS(timeNowNS(), d, h, m, s, ms, us, ns);
   write("Gear up at %d days, %d::%d::%d,%d.%d.%d", d, h, m, s, ms, us, ns);
}
```

## Availability

| Since Version |
|---|
