# FRstress CAPL Functions

> Category: `FRStress` | Type: `notes`

## Description

Control

Disturbance Configuration

Event Procedures

General Configuration

Operating Mode Configuration

Trigger Configuration

Trigger Output Configuration

FRstress | FlexRay | Exemplary Usage of FlexRay Functions in CAPL

| FRSTRESS Only available with option .FlexRay and FRstress hardware. |
|---|

| Control Disturbance Configuration Event Procedures General Configuration | Operating Mode Configuration Trigger Configuration Trigger Output Configuration |
|---|---|

| Functions | Short Description |
|---|---|
| FRSEnableTrigDist | Activates a trigger/disturbance page of FRstress. |
| FRSInit | Initializes FRstress. |
| FRSQuit | Ends the FRstress software. |
| FRSStart | Activates the hardware for the error disturbance activity. |
| FRSStop | Stops the current disturbance activity of the hardware. |
| FRSSoftwareTrigger | Activates the FRstress software trigger. |

| Functions | Short Description |
|---|---|
| FRSActivateCRCCalc | Activates the automatic CRC computation. |
| FRSSetBitstreamDist | Configures a bit sequence as disturbance. |
| FRSSetDistCount | Configures the number of disturbances. |
| FRSSetDistPayload | Adds frame Payload areas to a disturbance. |
| FRSSetDist | Adds frame elements (bit sequence) to a bit accuracy disturbance. |
| FRSSetDistElem | Adds frame elements (numeric input) to a bit accuracy disturbance. |

| Event Procedures | Short Description |
|---|---|
| FRSOnFinished | Registers a callback. |
| FRSOnStopped |  |

| Functions | Short Description |
|---|---|
| FRSClear | Clears the content of the current configuration. |
| FRSGetDevice | Indicates the device number of the available FRstress hardware. |
| FRSOpen | Opens an FRstress configuration file. |
| FRSSetDevice | Sets the device number for FRstress. |

| Functions | Short Description |
|---|---|
| FRSSetAnalogMode | Activates the analog disturbance mode. |
| FRSSetDigitalMode | Activates the digital disturbance mode. |
| FRSSetScopeMode | Activates the Scope mode. |

| Functions | Short Description |
|---|---|
| FRSSetTrig | Adds frame elements (bit sequence) to a trigger condition. |
| FRSSetTrigElem | Adds frame elements (numerical input) to a trigger condition. |
| FRSSetTrigPayload | Adds frame payload areas to a trigger condition. |
| FRSSetTrigPort | Sets the input port for the trigger condition in digital mode. |

| Functions | Short Description |
|---|---|
| FRSSetTrigOutput | Configures the trigger output. |

| Version 15© Vector Informatik GmbH |
|---|
