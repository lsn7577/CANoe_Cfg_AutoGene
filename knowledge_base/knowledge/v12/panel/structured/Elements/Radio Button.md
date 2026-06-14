# Radio Button

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The Radio Button can be used as a control and display element for triggering or displaying one option from a list of related options.

The following use cases are possible with the Radio Button:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

## Control Element

If you select the option during runtime of CANoe/CANalyzer, the switching value that you set in the Switch Value/Check property will be assigned to the symbol of the switching value.

## Display Element

The symbol is not set manually. Rather, it is set to a particular value, e.g., by simulation or CAPL programs, that is configured as a switching value in the Panel Designer. The option automatically appears as selected.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

General Group

General

Name

Control Name

Here you change the name of the control. This name and the name of the panel is required for access from CAPL.

Text

Here you change the description of the control.

Display Only

With a click on the symbol you switch between control and display element.

With activated option the control is used as display element.

—

Is Visible At Runtime

Specifies whether the control is to be displayed during runtime.

| Ribbon | Properties Window | Description |  |  |
|---|---|---|---|---|
| General Group | General |  |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |  |  |
| Text | Text | Here you change the description of the control. |  |  |
| Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |  |  |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |  |  |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |  |  |
| Font Group | Font |  |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |  |
| — | With a click on the symbol you increase the font size. |  |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |  |
| Font\|Underline | With a click on the symbol you underline the text. |  |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |  |
| Text Color | Here you change the color of the text. CAPL Access With the function setControlForeColor, you can change the Text Color of the Radio Button. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |  |
| Background Color | Here you change the background color of the text. CAPL Access With the function setControlBackColor, you can change the Background Color of the Radio Button. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |  |
| Text Align | With a click on the symbol you align the text on the left site of the control. |  |  |  |
| Text Align | With a click on the symbol you align the text in the middle of the control. |  |  |  |
| Text Align | With a click on the symbol you align the text on the right site of the control. |  |  |  |
| Switch Value Group | Switch Value |  |  |  |
| Activated | Activated | Here you change the switch value for the control. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. |  |  |
| — | Epsilon | If the linked symbol is a double value, then a value may not be detected if it differs from the expected value because of an approximation of the decimal.Via the Epsilon property, you may set in the Panel Designer a value that specifies up to which tolerated inaccuracy a value is detected. Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. Note This setting shall explicitly not be used for displaying ranges of values. | Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. | Note This setting shall explicitly not be used for displaying ranges of values. |
| Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. |  |  |  |  |
| Note This setting shall explicitly not be used for displaying ranges of values. |  |  |  |  |
| Check Position Group | Appearance |  |  |  |
| Check Position | Here you change the alignment of the Radio Button (not of the description) within the control: Top LeftAlign Radio Button at the top left Top RightAlign Radio Button at the top right Center LeftAlign Radio Button center left Center RightAlign Radio Button center right |  |  |  |
| More Group | — |  |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |  |
| Group: — | Layout |  |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |  |
| Group: — | Symbol |  |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. See also Configuration of the control. Valid Data Types of Symbols |  |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |  |

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

Switch Value Group

Switch Value

Activated

Here you change the switch value for the control. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value.

—

Epsilon

If the linked symbol is a double value, then a value may not be detected if it differs from the expected value because of an approximation of the decimal.Via the Epsilon property, you may set in the Panel Designer a value that specifies up to which tolerated inaccuracy a value is detected.

Note

The control has been configured with a Value = 2 and an Epsilon = 0.01.

If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status.

This setting shall explicitly not be used for displaying ranges of values.

Check Position Group

Appearance

Check Position

Here you change the alignment of the Radio Button (not of the description) within the control:

More Group

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Layout

Location/Size

Here you can enter settings relating to the size and position of the control.

You can also resize the control by dragging its markers.

Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel.

Symbol

You can assign a symbol to the control.

With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter.

See also Configuration of the control.

Valid Data Types of Symbols

Symbol Filter

Here you select the type of the symbol you want to assign to your control.

Assigning Controls

| Note The control has been configured with a Value = 2 and an Epsilon = 0.01. If the control receives a symbol value of 2.000000001 or 1.99999999997, then the value 2 is detected as valid and the control changes its status.If the value 2.05 is received, the control does not change its status. |
|---|

| Note This setting shall explicitly not be used for displaying ranges of values. |
|---|

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
