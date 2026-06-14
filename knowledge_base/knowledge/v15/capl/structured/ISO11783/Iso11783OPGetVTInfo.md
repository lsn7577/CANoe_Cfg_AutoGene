# Iso11783OPGetVTInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPGetVTInfo( dword ecuHandle, char key[] );
```

## Description

During initialization phase the Object Pool API request some information about the capabilities from Virtual Terminal. These information can be get with this function.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | Handle of the ECU. The handle must be created with Iso11783CreateECU. |
| "VersionNumber“ | Get memory |
| "NavigationSoftKeyCount" | Get number of Soft Keys |
| "SoftKeyWidth" | Get width of Soft Keys |
| "SoftKeyHeight" | Get height of Soft Keys |
| "VirtualSoftKeyCount" | Get number of virtual Soft Keys |
| "PhysicalSoftKeyCount" | Get number of physical Soft Keys |
| "SmallFontSizes" | Get Text Font Data |
| "LargeFontSizes" | Get Text Font Data |
| "FontTypeAttribute" | Get Text Font Data |
| "BootTime" | Get Hardware |
| "GraphicType" | Get Hardware |
| "Hardware" | Get Hardware |
| "Width" | Get Hardware |
| "Height" | Get Hardware |

## Example

```c
LONG vtWidth;
vtWidth = Iso11783OPGetVTInfo( handle, "Width" );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
