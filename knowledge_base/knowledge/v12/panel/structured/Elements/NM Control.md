# NM Control

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Cases

The NM Control can be used as a control and display element. With the NM Control you can control the OSEK NM DLL (oseknm01.dll) or the AutoSAR NM DLLs (AsrNM30.dll, AsrNM33.dll) on a simulated CAN bus in CANoe.

## Configuration

You can not assign a symbol to the NM Control. The corresponding system variables are assigned to the NM Control automatically.

Controlling during Run-Time

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

| Ribbon | Properties Window | Description |  |
|---|---|---|---|
| General Group | General |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. With the function enableControl, you can activate and deactivate the NM Control. |  |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |  |
| Font Group | Font |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |
| — | With a click on the symbol you increase the font size. |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |
| Font\|Underline | With a click on the symbol you underline the text. |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |
| Text Color | Here you change the color of the text. CAPL Access With the function setControlForeColor, you can change the Text Color of the NM Controls. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Background Color | Here you change the background color of the text. CAPL Access With the function setControlBackColor, you can change the Background Color of the NM Controls. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Settings Group | Settings |  |  |
| Network | Network | Here you select the network whose nodes are to be displayed. |  |
| Display | Number Interpretation | Here you change the display of the values within the NM Control: decimal hexadecimal |  |
| Auto Size | Auto Size With a click on the symbol you adapt the size of the NM Control automatically to the number of nodes so that no scrollbars are visible. The size that is predefined at the time of design is then overwritten. If you select true the size of the panel will be adapted to the size of the NM Control.You can only set the property to true if no other control besides the NM Control has been inserted on the panel. As soon as you position other controls on the panel at the time of design or manually change the size of the NM Control, Auto Size is set to false. |  |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |

## CAPL Access

—

Tab Index

Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime.

Font Group

Font

Font|Name/Size

Here you change the font and the font size.

With a click on the symbol you increase the font size.

With a click on the symbol you reduce the font size.

Font|Bold

With a click on the symbol you format the text bold.

Font|Italic

With a click on the symbol you format the text italic.

Font|Underline

With a click on the symbol you underline the text.

Font|Strikeout

Here you strikeout the text.

Font|Unit

Here you change the unit of the font size.

Text Color

Here you change the color of the text.

## CAPL Access

Background Color

Here you change the background color of the text.

## CAPL Access

Settings Group

Settings

Network

Here you select the network whose nodes are to be displayed.

Display

Number Interpretation

Here you change the display of the values within the NM Control:

Auto Size

With a click on the symbol you adapt the size of the NM Control automatically to the number of nodes so that no scrollbars are visible. The size that is predefined at the time of design is then overwritten.

If you select true the size of the panel will be adapted to the size of the NM Control.You can only set the property to true if no other control besides the NM Control has been inserted on the panel. As soon as you position other controls on the panel at the time of design or manually change the size of the NM Control, Auto Size is set to false.

More Group

—

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Layout

Location/Size

Here you can enter settings relating to the size and position of the control.

Note

You can also resize the control by dragging its markers.

Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel.

Steuerelemente zuweisen

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
