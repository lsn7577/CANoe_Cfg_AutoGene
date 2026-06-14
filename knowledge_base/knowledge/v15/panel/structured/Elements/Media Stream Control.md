# Media Stream Control

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Cases

The Media Stream Control is used to play streaming media received from the network (audio and video).

The following use cases are possible with the Media Stream Control:

## Configuration

The capability of the control to render streaming media depends on the format of the streaming content on the network and the availability of a codec used for decoding this streaming content.

The following network protocols are supported:

## Ribbon|Properties Tab

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

General Group

General

Name

Control Name

Here you change the name of the control. This name and the name of the panel is required for access from CAPL.

—

Is Visible At Runtime

Specifies whether the control is to be displayed during runtime.

| Ribbon | Properties Window | Description |
|---|---|---|
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| More Group | — |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |
| Group: — | Appearance |  |
| — | Border Style | Here you change the frame of the control: Fixed 3D3D frame Fixed SingleSingle frame NoneNo frame |
| — | Media Streams | Here, you configure the network media streams that should be played. Once the stream with the configured Stream ID is received during the measurement it is automatically played. |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

More Group

—

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Appearance

Border Style

Here you change the frame of the control:

Media Streams

Here, you configure the network media streams that should be played. Once the stream with the configured Stream ID is received during the measurement it is automatically played.

Assigning Controls
