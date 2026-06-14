# Panel Control Button

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

With the Panel Control Button you can open Panels during the measurement.

Note: Why is there also a Panel Control Button?

CANoe/CANalyzer distinguishes between the following panels:

If a panel is configured in the CANoe/CANalyzer configuration as well as in the Panel Control Button, it is treated as a panel of the CANoe/CANalyzer configuration.

You can use the Panel Control Button to open several referenced panels of an application range at the touch of a button and, at the same time, to automatically close referenced panels that are no longer needed.

The following use cases are possible with the Panel Control Button:

| Note: Why is there also a Panel Control Button? CANoe/CANalyzer distinguishes between the following panels: Panels that are assigned to the CANoe/CANalyzer configuration (Home ribbon tab\|Panel Configuration) Panels that are not assigned to the CANoe/CANalyzer configuration and are configured using the Panel Control Button. These are identified as referenced panels and appear in the list of referenced panels in the above-mentioned dialog. If a panel is configured in the CANoe/CANalyzer configuration as well as in the Panel Control Button, it is treated as a panel of the CANoe/CANalyzer configuration. |
|---|

## Configuration

Create a panel in the Panel Designer to which you add the Panel Control Button. Select the referenced panels. Save the panel and add it to the CANoe/CANalyzer configuration.

During runtime of CANoe/CANalyzer, you can open the selected panels and close panels that are no longer needed at the touch of a button. Panels that are assigned to the CANoe/CANalyzer configuration are not considered, i.e., they will not be closed.

You can configure the control via the ribbon or the Properties Window.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

General Group

General

Name

Control Name

Here you change the name of the control. This name and the name of the panel is required for access from CAPL.

Text

Here you change the description of the control.

—

Is Visible At Runtime

Specifies whether the control is to be displayed during runtime.

| Ribbon | Properties Window | Description |  |
|---|---|---|---|
| General Group | General |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |
| Text | Text | Here you change the description of the control. |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |  |
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
| Text Color | Here you change the color of the text. CAPL Access With the function setControlForeColor, you can change the Text Color of the Panel Control Button. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Background Color | Here you change the background color of the text. CAPL Access With the function setControlBackColor, you can change the Background Color of the Panel Control Button. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Text Align | With a click on the symbol you align the text on the left site of the control. |  |  |
| Text Align | With a click on the symbol you align the text in the middle of the control. |  |  |
| Text Align | With a click on the symbol you align the text on the right site of the control. |  |  |
| Appearance Group | Appearance |  |  |
| Image File | Image File | Here you change the background image for the control. |  |
| — | Image Align | If a image is assigned to the Button you can change the position of the image here. |  |
| — | Border Color | Here you change the color of the frame. This setting depends on the set Button Style. |  |
| — | Button Style | Here you change the style of the button. Dependent on this setting Background Color, Border Color and Hover Color can be changed. |  |
| — | Hover Color | Here you change the color the button should taken over if you hover with the mouse over it. This setting depends on the set Button Style. |  |
| — | Transparent Color | Change the transparent color. The picture transparency is always active. You must only define the color for which the picture should be transparent. |  |
| — | Use Transparent Color | Here you can set if the transparency should really be used. |  |
| — | Use Windows Style | Here you select whether the set background color Background Color is to be taken into account when Windows styles are used: If this property is True, the button is always displayed in the respective style, and the set background color is ignored. If this property is False, the set background color is taken into account. In the Windows style classic, the set background color is always taken into account, regardless of this property. Note The display of the Background Color depends on the Use Windows Style setting. | Note The display of the Background Color depends on the Use Windows Style setting. |
| Note The display of the Background Color depends on the Use Windows Style setting. |  |  |  |
| Settings Group | Settings |  |  |
| Referenced Panels | Referenced Panels With a click on the symbol you open the Referenced Panels dialog. Here you can define which panels will be opened when clicking the Panel Control Button.No Panel Editor panels (CNP) can be referenced. |  |  |
| — | Network Panels | Opens the Referenced Panels dialog. Here you can define which Network Panels will be opened when clicking the Panel Control Button.If you expand the Network Panels property, the selected Rx nodes are displayed (network name::node name). |  |
| — | Node Panels | Opens the Referenced Panels dialog. Here you can define which Node Panels will be opened when clicking the Panel Control Button.If you expand the Node Panels property, the selected Tx nodes are displayed (network name::node name). |  |
| — | Close All Other Referenced Panels | Indicates whether panels that were not explicitly added to the configuration but only referenced by other control buttons are to be closed. |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

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

Text Align

With a click on the symbol you align the text on the left site of the control.

With a click on the symbol you align the text in the middle of the control.

With a click on the symbol you align the text on the right site of the control.

Appearance Group

Appearance

Image File

Here you change the background image for the control.

—

Image Align

If a image is assigned to the Button you can change the position of the image here.

Border Color

Here you change the color of the frame. This setting depends on the set Button Style.

Button Style

Here you change the style of the button. Dependent on this setting Background Color, Border Color and Hover Color can be changed.

Hover Color

Here you change the color the button should taken over if you hover with the mouse over it. This setting depends on the set Button Style.

Transparent Color

Change the transparent color.

The picture transparency is always active. You must only define the color for which the picture should be transparent.

Use Transparent Color

Here you can set if the transparency should really be used.

Use Windows Style

Here you select whether the set background color Background Color is to be taken into account when Windows styles are used:

In the Windows style classic, the set background color is always taken into account, regardless of this property.

Note

The display of the Background Color depends on the Use Windows Style setting.

Settings Group

Settings

Referenced Panels

With a click on the symbol you open the Referenced Panels dialog. Here you can define which panels will be opened when clicking the Panel Control Button.No Panel Editor panels (CNP) can be referenced.

Network Panels

Opens the Referenced Panels dialog. Here you can define which Network Panels will be opened when clicking the Panel Control Button.If you expand the Network Panels property, the selected Rx nodes are displayed (network name::node name).

Node Panels

Opens the Referenced Panels dialog. Here you can define which Node Panels will be opened when clicking the Panel Control Button.If you expand the Node Panels property, the selected Tx nodes are displayed (network name::node name).

Close All Other Referenced Panels

Indicates whether panels that were not explicitly added to the configuration but only referenced by other control buttons are to be closed.

More Group

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Layout

Location/Size

Here you can enter settings relating to the size and position of the control.

You can also resize the control by dragging its markers.

Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel.

Assigning Controls

| Note The display of the Background Color depends on the Use Windows Style setting. |
|---|

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
