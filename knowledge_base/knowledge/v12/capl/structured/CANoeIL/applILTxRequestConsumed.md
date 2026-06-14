# applILTxRequestConsumed

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
void applILTxRequestConsumed ( );
```

## Description

After the IL clamp 15 state (for ASR PDU IL Ignition state) has been enabled by ILActivateClamp15 (for ASR PDU IL ARILSetIgnitionState) or any wake-up-allowed signal is transmitted, then optionally this functions is called. Within this function the bus NM sleep timer should be restarted.

## Return Values

—

## Availability

| Since Version |
|---|
