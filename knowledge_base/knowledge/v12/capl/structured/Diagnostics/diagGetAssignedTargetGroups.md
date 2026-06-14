# diagGetAssignedTargetGroups

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DiagGetAssignedTargetGroups(DiagRequest request, dword& targetGroupFlagsOut);
```

## Description

Returns a bit mask where each bit represents a target group. The diagnostic description defines in which target group the object may be sent, and the bit for this group is set to 1 in the mask returned.

The position of the bit in the mask (0 for least significant bit) can be used to query the qualifier and name of the target group using DiagGetTargetGroupQualifier and DiagGetTargetGroupName.

## Return Values

Error code

## Availability

| Since Version |
|---|
