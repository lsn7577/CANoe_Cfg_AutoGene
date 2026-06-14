# Compass

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Cases

The Compass is used to display the cardinal points and the speed.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

The compass is composed of two controls. Therefore assign a symbol to the display of the cardinal points (Direction) and the display of the speed (Speed) in the Panel Designer.

If you assign one or several symbols to the compass using drag and drop or via the context menu, the Assign Symbols dialog is opened in which you can assign the symbols to the two controls on the compass (Direction and Speed). On the left side of the dialog, you can see all symbols which you have assigned to the compass. You can assign these symbols to the controls on the right side using drag and drop. Symbols which are already assigned to one of the two controls, are marked with .

Use to remove an already assigned symbol.

Note

If you want to remove a symbol assignment via the context menu command Detach Selected Symbols, a dialog opens in which you can select one or all assignments using .

You can configure the control via the ribbon or the Properties Window.

| Note If you drag a system variable of the type GPS::GPSData on the panel, a compass is automatically inserted and linked to the structure members Direction and Speed. If you drag a system variable of the type GPS::GPSData on a compass, the structure members Direction and Speed are automatically linked to the corresponding controls on the compass. If you drag symbols with the name Direction and Speed on a compass, they are automatically linked to the corresponding controls on the compass. |
|---|

## Display Element

During runtime of CANoe/CANalyzer the Compass indicates the current symbol value.

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
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |  |
| Speed Group | Speed Settings |  |  |
| Show Speed | Show With a click on the symbol you switch on and off the display of the speed below the compass rose. |  |  |
| Text | Text | Here you change the description above the speed display. The unit of the assigned symbol is automatically displayed in brackets. |  |
| Decimal Places | Decimal Places | Here you change the number of the decimal places for the display of the speed. |  |
| Text Font / Value Font Group | Font Text/Value |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |
| — | With a click on the symbol you increase the font size. |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |
| Font\|Underline | With a click on the symbol you underline the text. |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |
| Text Color | Here you change the color of the text. CAPL Access With the function setControlForeColor, you can change the Value Color for the display of the speed. |  |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |
| Group: — | Symbol |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. See also Configuration of the control. Valid Data Types of Symbols |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

Speed Group

Speed Settings

Show Speed

Show

With a click on the symbol you switch on and off the display of the speed below the compass rose.

Text

Here you change the description above the speed display. The unit of the assigned symbol is automatically displayed in brackets.

Decimal Places

Here you change the number of the decimal places for the display of the speed.

Text Font / Value Font Group

Font Text/Value

Font

Font|Name/Size

Here you change the font and the font size.

—

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

With the function setControlForeColor, you can change the Value Color for the display of the speed.

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

Symbol

You can assign a symbol to the control.

With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter.

See also Configuration of the control.

Valid Data Types of Symbols

Symbol Filter

Here you select the type of the symbol you want to assign to your control.

Assigning Controls

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
