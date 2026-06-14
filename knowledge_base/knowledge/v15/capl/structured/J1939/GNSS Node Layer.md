# GNSS Node Layer

> Category: `J1939` | Type: `notes`

## Description

Events

Node Control

Other Function

Settings

Simulation

Waypoints

Error Codes GNSSAppErrorIndication | Error Codes GNSSGetLastError

| J1939 Only available with J1939. To use the CAPL functions the node layer GNSS_NL.DLL must be included. You can include the node layer by using the configuration dialog of the node on page Components or via the node attribute NodeLayerModules in the database. |
|---|

| Events Node Control Other Function | Settings Simulation Waypoints |
|---|---|

| Function | Short Description |
|---|---|
| GNSSAppAddrClaimed | Identifies an Address Claiming procedure that was performed successfully. |
| GNSSAppCmdAddrIndication | Indicates that a new address has been assigned to the node. |
| GNSSAppErrorIndication | Identifies errors. |
| GNSSOnLastWpReached | Is called when the last waypoint of the waypoint list has been reached. |
| GNSSOnSetSpeed | Is called if the speed of the simulation has been changed. |
| GNSSOnWpBeforeLastReached | Is called when the next-to-last waypoint of the waypoint list has been reached. |

| Function | Short Description |
|---|---|
| GNSSGetAddress | Returns a network address. |
| GNSSGetName | Returns the J1939 device name of a control device. |
| GNSSMakeName | Generates a J1939 device name. |
| GNSSShutDown | Removes the node from the network. |
| GNSSStartUp | Sets up a logical node within a CANoe network node. |
| GNSSUpdateTable | Updates the network table. |

| Function | Short Description |
|---|---|
| GNSSGetAbsFilePath | Gets the absolute path of a file. |
| GNSSGetLastError | Returns the error status of the last executed function. |

| Function | Short Description |
|---|---|
| GNSSSetCOGSOGVal | Changes the value of the parameter group COG&SOG, Rapid Update. |
| GNSSSetJitterAlt | Sets the jitter by which the altitude deviates from its nominal value. |
| GNSSSetJitterLatLon | Sets the jitter by which the longitudinal and latitudinal degree deviates from the respective nominal value. |
| GNSSSetPGSettings | Changes the values of individual parameter groups. |
| GNSSSetPosDataVal | Changes the value of the parameter group GNSS Position Data. |
| GNSSSetUnits | Determines the system of measurement units. |

| Function | Short Description |
|---|---|
| GNSSContinueSpeed | Restores an old speed. |
| GNSSGetCurCourse | Returns the current course of the GNSS receiver. |
| GNSSGetCurGradient | Returns the current gradient of the GNSS receiver. |
| GNSSGetCurSpeed | Returns the current speed at which the GNSS receiver is moving. |
| GNSSPauseSpeed | Sets the speed to zero, temporarily. |
| GNSSSetCourse | Determines a new course and a new gradient for the GNSS receiver. |
| GNSSSetSpeed | Sets the speed at which the GNSS receiver moves. |
| GNSSStartSimulation | Starts the simulation. |
| GNSSStopSimulation | Stops the simulation. |

| Function | Short Description |
|---|---|
| GNSSAddWp | Inserts a new waypoint at the end of the waypoint list. |
| GNSSAddWpFile | Inserts the GNSS positions of a file into the waypoint list. |
| GNSSAddWpLine | Describes a line. |
| GNSSAddWpMeander | Describes a meander with rounded off corners. |
| GNSSAddWpRect | Describes a rectangle with rounded off corners. |
| GNSSAddWpRef | Inserts a new waypoint at the end of the waypoint list. |
| GNSSAddWpRefS | Inserts a new waypoint at a given speed at the end of the waypoint list. |
| GNSSAddWpRel | Inserts a new waypoint at the end of the waypoint list. |
| GNSSAddWpRelS | Inserts a new waypoint at a given speed at the end of the waypoint list. |
| GNSSAddWpS | Inserts a new waypoint at a given speed at the end of the waypoint list. |
| GNSSGetCurAlt | Returns the current altitude at which the receiver is located. |
| GNSSGetCurLat | Returns the current latitude at which the receiver is located. |
| GNSSGetCurLon | Returns the current longitude at which the receiver is located. |
| GNSSRemoveWp | Deletes all waypoints of the waypoint list. |
| GNSSSetRefPoint | Defines reference points. |

| Version 15© Vector Informatik GmbH |
|---|
