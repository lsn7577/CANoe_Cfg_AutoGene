# DoIP_SetRoutingActivationOEMSpecific

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetRoutingActivationOEMSpecific(long sendOEMSpecific, dword OEMspecific);
```

## Description

Sets the OEM-specific parameters in the Routing Activation Request Message.

## Return Values

—

## Example

The message can also be configured from the DoIP.INI file

```c
// Send a constant in the RAR message
DoIP_SetRoutingActivationOEMSpecific( 1, 0x31425927);
```

## Availability

| Since Version |
|---|
