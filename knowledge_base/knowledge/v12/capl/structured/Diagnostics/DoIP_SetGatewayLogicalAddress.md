# DoIP_SetGatewayLogicalAddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetGatewayLogicalAddress(dword logicalAddress);
```

## Description

Sets the logical address of the gateway that responds to a vehicle announcement request.

## Return Values

—

## Example

```c
DoIP_SetVehicleLogicalAddress( 0x201);
DoIP_SetGatewayLogicalAddress( 0x100);
DoIP_ConnectToVehicle();
// if the gateway with logical address 0x0100 responds to the vehicle
// identification request, the connection can be made even though the ECU
// with logical address 0x0201 is the target of the communication
```

## Availability

| Since Version |
|---|
