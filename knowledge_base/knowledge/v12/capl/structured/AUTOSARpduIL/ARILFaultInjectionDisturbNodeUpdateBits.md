# ARILFaultInjectionDisturbNodeUpdateBits

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILFaultInjectionDisturbNodeUpdateBits (long flags, long disturbanceMode, long disturbanceCount, long disturbanceValue);
```

## Description

Disturbs the Update Bit of all signals and/or signal groups that are sent by the current node (see Update Bit).

## Parameters

| Name | Type | Description |
|---|---|---|
| Mask | Value | Description |
| 0x3 | 0 | Disturbs signal and signal group update bits of node. |
| 0x3 | 1 | Disturbs only signal update bits of node. |
| 0x3 | 2 | Disturbs only signal group update bits of node. |
| 0x3 | 3 | reserved |
| 0xFFFFFFFC | all | reserved |

## Return Values

0: No error.

## Availability

| Since Version |
|---|
