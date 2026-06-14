# ARILConfigureNMNotifications

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
dword ARILConfigureNMNotifications (dword dir, dword mode);
```

## Description

This function has impact on the (automatic) coupling between IL and NM on the IL side.

Normally, there exists an automatic notification between IL and NM. This can be broken by implementation of dedicated call-back functions for IL and NM. This function defines to take or ignore those notifications always, regardless of existing callbacks.

Remember, an appropriate function can also be called on NM side!

## Return Values

0: No error

## Availability

| Since Version |
|---|
