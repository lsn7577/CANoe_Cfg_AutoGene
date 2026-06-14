# Group Box

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The Group Box is a static element and serves to combine multiple elements.

The following use cases are possible with the Group Box:

## Configuration

Drag the relevant controls to the Group Box in the Panel Designer. The font type and size of the Group Box is assigned automatically to the controls.

Use the snaplines that appear to arrange the controls as required.

Note

When you move the Group Box, all the controls inside it will move too, but this will not affect how they are arranged within the box.

You can configure the control via the ribbon or the Properties Window.

The Group Box and the elements it contains are displayed during runtime of CANoe/CANalyzer.

| Note When you move the Group Box, all the controls inside it will move too, but this will not affect how they are arranged within the box. |
|---|

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
| Text Color | Here you change the color of the text. |  |  |
| Background Color | Here you change the background color of the text. |  |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Appearance |  |  |
| — | Use Windows Style | Here you select whether the set background color Background Color is to be taken into account when Windows styles are used: If this property is True, the button is always displayed in the respective style, and the set background color is ignored. If this property is False, the set background color is taken into account. In the Windows style classic, the set background color is always taken into account, regardless of this property. Note The display of the Background Color depends on the Use Windows Style setting. | Note The display of the Background Color depends on the Use Windows Style setting. |
| Note The display of the Background Color depends on the Use Windows Style setting. |  |  |  |
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

Background Color

Here you change the background color of the text.

More Group

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Appearance

Use Windows Style

Here you select whether the set background color Background Color is to be taken into account when Windows styles are used:

In the Windows style classic, the set background color is always taken into account, regardless of this property.

Note

The display of the Background Color depends on the Use Windows Style setting.

Layout

Location/Size

Here you can enter settings relating to the size and position of the control.

You can also resize the control by dragging its markers.

Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel.

| Assigning Controls |

| Note The display of the Background Color depends on the Use Windows Style setting. |
|---|

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
