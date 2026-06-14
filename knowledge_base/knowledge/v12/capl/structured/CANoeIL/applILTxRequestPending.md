# applILTxRequestPending

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
void applILTxRequestPending ( );
```

## Description

If the IL clamp 15 state (for ASR PDU IL Ignition state) is being enabled by ILActivateClamp15 (for ASR PDU IL ARILSetIgnitionState) or any wake-up-allowed signal is changed, then optionally this functions is called. Within this function the bus should be requested by the network management DLL.

## Return Values

—

## Availability

| Since Version |
|---|
