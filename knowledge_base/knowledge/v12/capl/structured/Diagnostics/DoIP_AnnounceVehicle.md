# DoIP_AnnounceVehicle

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_AnnounceVehicle();
```

## Description

Starts broadcasting Vehicle Announcement Messages.

The timing parameter A_DoIP_Announce_Wait in the DoIP.INI file as well as the parameter toInitial_ms configured with the function DoIP_ConfigureVehicleAnnouncement are ignored when using this function, i.e. sending the Vehicle Announcement Messages starts without delay.

## Return Values

—

## Example

The number of messages sent and the time between sends can be configured in the DoIP.INI file and via DoIP_ConfigureVehicleAnnouncement.

```c
// Start broadcasting Vehicle Announcement Messages
DoIP_AnnounceVehicle();
```

## Availability

| Since Version |
|---|
