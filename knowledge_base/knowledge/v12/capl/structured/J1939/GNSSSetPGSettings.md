# GNSSSetPGSettings

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetPGSettings( dword pgn, dword enable, dword destination, dword priority, dword updateRate )
```

## Description

This function can be used to change the values of individual parameter groups. So far, the NMEA 2000® parameter groups “GNSS Position Data” (PGN 129029), “Position Delta, High Precision Rapid Update” (PGN 129027), “Position, Rapid Update” (PGN 129025), and “COG & SOG, Rapid Update” (PGN 129026) as well as the J1939 parameter groups "VehiclePosition" (PGN 65267) and “Vehicle Direction/Speed” (PGN 65256) are supported.

By default “Vehicle Direction/Speed” is not transmitted cyclically. But if enabled this message can be requested by a request message.

When a node is reached with GNSSStartUp, the following start values are set:

129029

1

255

3

1000

129027

0

2

100

129025

129026

250

65267

6

65256

Thus the first both parameter groups are transferred if this function is not called.

The function is only performed successfully if the simulation has not yet been started.

## Return Values

error code

## Example

```c
// disable PG “Position, Rapid Update”
GNSSSetPGSettings( 129025, 0, 255, 3, 1000 );
```

## Availability

| Since Version |
|---|
