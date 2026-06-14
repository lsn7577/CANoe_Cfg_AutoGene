# Iso11783IL_OPGetVTInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPGetVTInfo( char key[] ); // form 1
long Iso11783IL_OPGetVTInfo( dbNode implement, char key[] ); // form 2
```

## Description

During initialization phase the Object Pool API request some information about the capabilities from Virtual Terminal. These information can be get with this function.

## Parameters

| Name | Type | Description |
|---|---|---|
| Key | Message | Description |
| "VersionNumber“ | Get memory | Supported VT version. |
| "NavigationSoftKeyCount" | Get number of Soft Keys | The number of Physical Soft Keys that are used by the VT for navigation among the Virtual Soft Keys. |
| "SoftKeyWidth" | Get number of Soft Keys | Number of pixels on the x-axis for a Soft Key descriptor. |
| "SoftKeyHeight" | Get number of Soft Keys | Number of pixels on the y-axis for a Soft Key descriptor. |
| "VirtualSoftKeyCount" | Get number of Soft Keys | Number of possible virtual Soft Keys in a Soft Key Mask. |
| "PhysicalSoftKeyCount" | Get number of Soft Keys | Number of Physical Soft Keys. |
| "SmallFontSizes" | Get Text Font Data | Supported small font sizes. |
| "LargeFontSizes" | Get Text Font Data | Supported large font sizes. |
| "FontTypeAttribute" | Get Text Font Data | Supported font styles. |
| "BootTime" | Get Hardware | Maximum number of seconds from a VT power startup. |
| "GraphicType" | Get Hardware | Supported graphic modes. |
| "Hardware" | Get Hardware | Supported hardware features. |
| "Width" | Get Hardware | Number of divisions on the horizontal axis in the Data Mask Area. |
| "Height" | Get Hardware | Number of divisions on the vertical axis in the Data Mask Area. |
| implement |  | Simulation node to apply the function. |

## Example

```c
LONG vtWidth;
vtWidth = Iso11783IL_OPGetVTInfo( "Width" );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1 9.0: form 2 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
