# canDisturbanceSequence::AppendToSequence

> Category: `CANDisturbance` | Type: `function`

## Syntax

```c
void canDisturbanceSequence::AppendToSequence(word segmentLength, char segmentValue);
```

## Description

Adds a segment to a sequence. If the maximum number of segments is reached, the function always returns 0.

Maximum number of segments: 4096

## Return Values

1: Segment is added to the sequence

## Availability

| Since Version |
|---|
