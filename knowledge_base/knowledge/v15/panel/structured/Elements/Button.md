# Button

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The Button is a control with which assigned actions can be triggered.

The following uses cases are possible with the Button:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

## Control Element

If you click the Button during runtime of CANalyzer, the value that you set in the Pressed property will be assigned to the symbol. Setting this value causes a stored action to be triggered.If you release the Button, the symbol receives the value that you have set in the Released property. This symbol value can also be used to trigger an action.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

General Group

General

Name

Control Name

Here you change the name of the control. This name and the name of the panel is required for access from CAPL.

Text

Here you change the description of the control.

| Ribbon | Properties Window | Description |  |
|---|---|---|---|
| General Group | General |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |
| Text | Text | Here you change the description of the control. CAPL Access With the function setControlProperty, you can set this property of the control. |  |
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
| Text Color | Here you change the color of the text. CAPL Access With the function setControlForeColor, you can change the Text Color of the Button. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Background Color | Here you change the background color of the text. CAPL Access With the function setControlBackColor, you can change the Background Color of the Button. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Text Align | With a click on the symbol you align the text on the left site of the control. |  |  |
| Text Align | With a click on the symbol you align the text in the middle of the control. |  |  |
| Text Align | With a click on the symbol you align the text on the right site of the control. |  |  |
| Switch Values Group | Switch Values |  |  |
| Pressed | Pressed | Here you change the symbol value that is set when the button is clicked. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. |  |
| Released | Released | Here you change the symbol value that is set when the button is released. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Appearance |  |  |
| — | Border Color | Here you change the color of the frame. This setting depends on the set Button Style. |  |
| — | Button Style | Here you change the style of the button. Dependent on this setting Background Color, Border Color and Hover Color can be changed. |  |
| — | Hover Color | Here you change the color the button should taken over if you hover with the mouse over it. This setting depends on the set Button Style. |  |
| — | Image | Here you can assign a image to the Button. |  |
| — | Image Align | If a image is assigned to the Button you can change the position of the image here. |  |
| — | Transparent Color | Change the transparent color. The picture transparency is always active. You must only define the color for which the picture should be transparent. |  |
| — | Use Transparent Color | Here you can set if the transparency should really be used. |  |
| — | Use Windows Style | Here you select whether the set background color Background Color is to be taken into account when Windows styles are used: If this property is True, the button is always displayed in the respective style, and the set background color is ignored. If this property is False, the set background color is taken into account. In the Windows style classic, the set background color is always taken into account, regardless of this property. Note The display of the Background Color depends on the Use Windows Style setting. | Note The display of the Background Color depends on the Use Windows Style setting. |
| Note The display of the Background Color depends on the Use Windows Style setting. |  |  |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |
| Group: — | Symbol |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. Valid Data Types of Symbols |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |

## CAPL Access

With the function setControlProperty, you can set this property of the control.

—

Is Visible At Runtime

Specifies whether the control is to be displayed during runtime.

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

Switch Values Group

Switch Values

Pressed

Here you change the symbol value that is set when the button is clicked. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value.

Released

Here you change the symbol value that is set when the button is released. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value.

More Group

—

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Appearance

Border Color

Here you change the color of the frame. This setting depends on the set Button Style.

Button Style

Here you change the style of the button. Dependent on this setting Background Color, Border Color and Hover Color can be changed.

Hover Color

Here you change the color the button should taken over if you hover with the mouse over it. This setting depends on the set Button Style.

Image

Here you can assign a image to the Button.

Image Align

If a image is assigned to the Button you can change the position of the image here.

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

Layout

Location/Size

Here you can enter settings relating to the size and position of the control.

You can also resize the control by dragging its markers.

Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel.

Symbol

You can assign a symbol to the control.

With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter.

Valid Data Types of Symbols

Symbol Filter

Here you select the type of the symbol you want to assign to your control.

Assigning Controls | Transparency Color

| Note The display of the Background Color depends on the Use Windows Style setting. |
|---|

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
