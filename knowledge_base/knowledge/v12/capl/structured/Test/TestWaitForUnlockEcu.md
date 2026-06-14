# TestWaitForUnlockEcu

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForUnlockEcu(long securityLevel); // form 1
```

## Description

This functions tries to unlock an ECU. It requests a seed, calculates the key with the Seed & Key DLL and sends it to the ECU. The Seed & Key DLL must be configured in the diagnostic configuration dialog.

The message exchange can be monitored with on DiagRequest/on DiagResponse event handler.

## Return Values

On success 0, otherwise error code

## Availability

| Since Version |
|---|
