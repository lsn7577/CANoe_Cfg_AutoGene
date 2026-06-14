# DoIP_SetVehicleAddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetVehicleAddress( char address[]);
```

## Description

Sets the address to be used by the DoIP layer. If given, the address is used to access the DoIP entity from the tester equipment, i.e. in case an IP address is used, a Vehicle Identification Request is omitted. In a vehicle simulation it will determine the adapter used for communication; in this case this function must be called in on preStart.

## Return Values

—

## Example

```c
// Set the vehicle ‘address’
char buffer[256];
DiagGetCommParameter( "DoIP.VEHICLE_Address",
                      0, buffer, elcount( buffer));
DoIP_SetVehicleAddress( buffer);
```

## Availability

| Since Version |
|---|
