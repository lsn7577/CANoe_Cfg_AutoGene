# timeDiff

> Category: `Other` | Type: `function`

## Syntax

```c
long timeDiff(message m1, NOW);
```

## Description

Time difference between messages or between a message and the current time in ms (msg2 - msg1 or now - msg1). Starting with CANalyzer 2.xx this difference can be calculated directly (Units of 10 microseconds).

## Return Values

Time difference in ms.

## Example

```c
diff = timeDiff(m100, now); // CANalyzer 1.x & 2.x
diff = this.time - m100.time; // CANalyzer 2.xx
```

## Availability

| Since Version |
|---|
