# GNSSAddWpFile

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSAddWpFile( byte filepath[], dword useTimeInfo )
```

## Description

The function deletes all waypoints in the waypoint list and then inserts the GNSS positions of a file into the list.

useTimeInfo = 0:

The waypoints are inserted without speed information (according to the GNSSAddWp function). The speed of the receiver is controlled by GNSSSetSpeed. The value kWaypoint must be used as a simulation mode in GNSSStartSimulation.

useTimeInfo = 1:

The speed is controlled by the file. Only GNSS positions from the file are used to which a time > 0 is assigned. The speed is calculated by means of the difference in time and space between two successive positions. The value kFile must be used as a simulation mode in GNSSStartSimulation.

## Return Values

error code

## Example

```c
char filePath[255] = “C:\log.pos”;
GNSSAddWpFile( 
 filePath, 1 );
```

## Availability

| Since Version |
|---|
