# GNSSSetPosDataVal

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetPosDataVal(dword fixSID, dword systemAndMethod, dword integrity, dword numOfSVs, dword hdop, dword pdop, dword geoSeparation, dword numOfRefStat, dword refStations[]}
```

## Description

This function can be used to change values of parameter group "GNSS Position Data" (PGN 129029) which are not modified by the simulation automatically.

The same settings can be made via node attributes in the used database.

## Return Values

error code

## Example

```c
dword refSta[2];
refStation[0] = 0x11110010;
refStation[1] = 0x22220020;
GNSSSetPosDataVal(0,0x20,1,4,21,54,763,2,refSta);
```

## Availability

| Since Version |
|---|
