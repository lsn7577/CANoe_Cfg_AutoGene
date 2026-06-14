# diagGetTargetGroupName

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DiagGetTargetGroupName(char ecuQualifier[], dword bitPos, char groupNameOut[]);
```

## Description

Returns the name of the diagnostic target group for which the bit at the given position is used by diagGetAssignedTargetGroups. If the target ECU is not specified explicitly, the target selected with diagSetTarget is used.

## Return Values

≥ 0: number of characters written

## Availability

| Since Version |
|---|
