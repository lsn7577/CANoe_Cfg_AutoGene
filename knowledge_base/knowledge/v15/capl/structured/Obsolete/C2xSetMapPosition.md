# C2xSetMapPosition

> Category: `Obsolete` | Type: `notes`

## Description

void SetMapPosition(){ float lat = 48.824990; float lon = 9.094568; C2xSetMapPosition(lat, lon);}

See Also

| Deprecated Function Replaced by SetMapPosition. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long C2xSetMapPosition( float latitude, float longitude ); |  |  |  |
| Function | Sets the map to a specific position. Note If the Auto-Follow option is enabled for a vehicle, the option will be disabled. | Note If the Auto-Follow option is enabled for a vehicle, the option will be disabled. |  |  |
| Note If the Auto-Follow option is enabled for a vehicle, the option will be disabled. |  |  |  |  |
| Parameters | latitude Latitude of the position where the map should jump |  |  |  |
| longitude Longitude of the position where the map should jump |  |  |  |  |
| Return Values | 0 if success, else the set went wrong |  |  |  |
| Availability | Since Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 8.5 SP4 | Car2x | — | • |  |
| Example void SetMapPosition(){ float lat = 48.824990; float lon = 9.094568; C2xSetMapPosition(lat, lon);} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
