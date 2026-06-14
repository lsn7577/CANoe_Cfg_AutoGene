# GNSSGetAddress

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSGetAddress( dword mask, byte [8] name)
```

## Description

The function returns a network address with which a control device that is described by the function parameters logged on to the network.

If no device is found for the described functionality, the NULL address (255) is returned. If the function fails, 0xFFFFFFFF will be returned.

The mask parameter is used to specify which parts of the name will be taken into consideration. To use the entire name, the value 0x1FF must be used for mask. The values of the following table can be linked with a logical OR to make it possible to consider only parts of the name. If the name applies to multiple nodes on the bus, only the address of the first node is returned.

## Parameters

| Name | Description |
|---|---|
| mask | Bit mask, only the masked bits of the name are used |
| name | Name of the device |

## Return Values

Address or 0xFFFFFFFF

## Example

```c
dword address;
address = GNSSGetAddress( 0x1FF, name );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | — |
| Restricted To | — | J1939 ISO11783 | J1939 ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
