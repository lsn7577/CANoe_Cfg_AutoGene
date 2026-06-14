# ARILFaultInjectionDisturbChecksum

> Category: `AUTOSARpduIL` | Type: `function`

## Syntax

```c
long ARILFaultInjectionDisturbChecksum (dbMessage, long type, long disturbanceMode, long disturbanceCount, long disturbanceValue);
```

## Description

Disturbs the CRC of a PDU or signal group (see CRC Value). The function without the parameter for the signal group will only disturb CRCs that are not part of a signal group.

## Return Values

0: No error.

## Availability

| Since Version |
|---|
