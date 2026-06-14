# _DoIP_VehicleAnnouncementInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_VehicleAnnouncementInd(char VIN[], WORD logAddr, BYTE entityIdent[], BYTE groupIdent[], BYTE furtherActionRequired, BYTE VINGIDsyncStatus)
```

## Description

A Vehicle Announcement Message (VAM) has been received, possibly as a Vehicle Identification Response for a Vehicle Identification Request (VIR) Message. The responding vehicle indicates its presence.

If the responding vehicle’s VIN or EID has been selected as VIR parameter, this vehicle will be selected for communication.

## Return Values

—

## Example

```c
void _DoIP_VehicleAnnouncementInd( char VIN[], WORD logAddr, BYTE entityIdent[], BYTE groupIdent[], BYTE furtherActionReq, BYTE VINGIDsyncStatus)
{
  WORD i;
  write( "[%.3f] Vehicle Announcement Message from '%s'", timenow()/100000.0, VIN);

  // Store the VIN of the responding vehicle in a table,
  // if it is not known already

  for( i = 0; i < gVehiclesFound; ++i)
  {
    if( 0 == strncmp( VIN, gVehicleAnswered[i], elcount(VIN)))
    return; // vehicle already registered, so do not store it again
  }

  if( gVehiclesFound < elcount( gVehicleAnswered))
  {
    strncpy( gVehicleAnswered[ gVehiclesFound], VIN, elcount( gVehicleAnswered[ gVehiclesFound]));
    ++gVehiclesFound;
  }
}
```

## Availability

| Since Version |
|---|
