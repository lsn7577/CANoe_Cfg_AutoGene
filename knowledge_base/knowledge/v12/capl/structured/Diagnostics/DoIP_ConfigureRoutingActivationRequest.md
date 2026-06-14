# DoIP_ConfigureRoutingActivationRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_ConfigureRoutingActivationRequest(long mode, dword activationType, dword valueReserved);
```

## Description

Configures the Routing Activation Request Message sent by a tester.

## Return Values

—

## Example

You can also configure these values in the DoIP.INI file.

```c
// Send the 2 byte activation type 0x1234, and set the reserved field
DoIP_ConfigureRoutingActivationRequest( 2, 0x1234, 0x76543210);
```

## Availability

| Since Version |
|---|
