# diagGetTargetGroupQualifier

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DiagGetTargetGroupQualifier(char ecuQualifier[], dword bitPos, char groupQualOut[]);
```

## Description

Returns the qualifier of the diagnostic target group for which the bit at the given position is used by diagGetAssignedTargetGroups. If the target ECU is not specified explicitly, the target selected with diagSetTarget is used.

## Return Values

≥ 0: number of characters written

## Availability

| Since Version |
|---|
