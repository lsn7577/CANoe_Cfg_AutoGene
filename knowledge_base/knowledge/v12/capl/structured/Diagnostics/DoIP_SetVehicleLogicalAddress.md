# DoIP_SetVehicleLogicalAddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetVehicleLogicalAddress(dword logicalAddress);
```

## Description

Sets vehicle logical DoIP address sent in DoIP PDUs.

## Return Values

—

## Example

The following example sets the Logical Address of a vehicle (used e.g. in Routing Activation Responses) and makes it known to the DoIP layer.

```c
dword gGatewayLogAddress = 0x1000;
write("Logical address of vehicle = 0x%04x", gGatewayLogAddress);
DoIP_SetVehicleLogicalAddress( gGatewayLogAddress);
DoIP_AddECU( gGatewayLogAddress);
```

## Availability

| Since Version |
|---|
