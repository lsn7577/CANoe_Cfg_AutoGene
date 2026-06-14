# DoIP_ConfigureVehicleAnnouncement

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_ConfigureVehicleAnnouncement(dword toInitial_ms, dword messageCount, dword toInterval_ms);
```

## Description

Configures when the Vehicle Announcement Messages are sent.

## Parameters

| Name | Description |
|---|---|
| Note This parameter is ignored, if the function DoIP_AnnounceVehicle is used for sending Vehicle Announcement Messages. |  |

## Return Values

—

## Example

```c
// Send 5 announcement messages after 200 ms, with 100 ms interval
DoIP_ConfigureVehicleAnnouncement( 200, 5, 100);
DoIP_AnnounceVehicle();
```

## Availability

| Since Version |
|---|
