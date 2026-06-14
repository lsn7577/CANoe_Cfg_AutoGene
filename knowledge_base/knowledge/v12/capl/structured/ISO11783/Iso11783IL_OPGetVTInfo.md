# Iso11783IL_OPGetVTInfo

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPGetVTInfo( char key[] ); // form 1
```

## Description

During initialization phase the Object Pool API request some information about the capabilities from Virtual Terminal. These information can be get with this function.

## Parameters

| Name | Description |
|---|---|
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

## Return Values

>= 0: Value

## Example

```c
LONG vtWidth;
vtWidth = Iso11783IL_OPGetVTInfo( "Width" );
```

## Availability

| Since Version |
|---|
