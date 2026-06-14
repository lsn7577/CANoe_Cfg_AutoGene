# ARILFaultInjectionDisturbSequenceCounter

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILFaultInjectionDisturbSequenceCounter (dbMessage, long type, long disturbanceMode, long disturbanceCount, long disturbanceValue, long continueMode);
```

## Description

Disturbs the SQC or TGL of a PDU or signal group (see Supported Features).

The function without the parameter for the signal group will only disturb SQCs or TGLs that are not part of a signal group.

## Return Values

0: No error.

## Availability

| Since Version |
|---|
