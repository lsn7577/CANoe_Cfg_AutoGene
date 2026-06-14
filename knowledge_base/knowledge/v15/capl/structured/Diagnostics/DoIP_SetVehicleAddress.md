# DoIP_SetVehicleAddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetVehicleAddress( char address[]);
```

## Description

Sets the address to be used by the DoIP layer. If given, the address is used to access the DoIP entity from the tester equipment, i.e. in case an IP address is used, a Vehicle Identification Request is omitted. In a vehicle simulation it will determine the adapter used for communication; in this case this function must be called in on preStart.

## Parameters

| Name | Description |
|---|---|
| address | The address of the DoIP layer. Can be a VIN, IPv4 address, IPv6 address or EID (Entity ID, typically a MAC address). Note: If an IPv4/IPv6 address is given as address, the Vehicle Identification Sequence is omitted. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 SP4 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
