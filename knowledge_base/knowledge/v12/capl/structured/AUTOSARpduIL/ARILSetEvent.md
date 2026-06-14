# ARILSetEvent

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILSetEvent (dbSignal)
```

## Description

This function considers Debounce Delay, and it also considers the activity of the network. So a call of this function will lead to a transmission of the associated PDU, if the network is active.

## Return Values

0: No error.

## Availability

| Since Version |
|---|
