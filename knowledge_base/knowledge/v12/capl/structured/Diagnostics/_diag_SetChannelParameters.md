# _diag_SetChannelParameters

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _Diag_SetChannelParameters ();
```

## Description

This function will be called after measurement start (in ECU simulations) or after diagSetTarget() (in test nodes) and enables the CAPL program to configure the transport protocol.

If the protocol is configured by the data base nothing has to be done.

## Return Values

—

## Availability

| Since Version |
|---|
