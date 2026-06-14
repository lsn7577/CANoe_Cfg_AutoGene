# Combo Box

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The Combo Box can be used as a control and display element for selecting or displaying symbolic values from value tables of a database or system variable definition.

The following use cases are possible with the Combo Box:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

Assign a symbol to the Combo Box in the Panel Designer.A value table with symbolic values must be assigned to the symbol so that the symbolic values can be selected and displayed during runtime of CANalyzer.

You can configure the control via the ribbon or the Properties Window.

## Control Element

During runtime of CANalyzer you can select a symbolic value in the Combo Box that is assigned to the symbol.

## Display Element

The symbol value is not set manually. Rather it is set by simulation or CAPL programs, for example. The Combo Box displays the symbolic value automatically.

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
| Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |  |  |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |  |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |  |
| Text Font / Combo Box Font Group | Font Text/Box |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |
| — | With a click on the symbol you increase the font size. |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |
| Font\|Underline | With a click on the symbol you underline the text. |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |
| Text Color | Here you change the color of the text. CAPL Access With the function setControlForeColor, you can change the Text Color of the label. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Background Color | Here you change the background color of the text. CAPL Access With the function setControlBackColor, you can change the Background Color of the label. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Appearance Group | Appearance |  |  |
| Combo Box Style | Here you change the list type: Drop Down List Simple list Flat Drop Down List |  |  |
| Display Text | Here you change the alignment of the description: Text LeftTo the left of the Combo Box Text RightTo the right of the Combo Box Text TopAbove the Combo Box Hide TextNo description |  |  |
| Display Rows | Here you change the number of displayed items: Show All ItemsAll available items are displayed in the list. Show Configured ItemsThe list only contains the number of entries specified by you under Number of Items. |  |  |
| Drop Down Max Items | Number of Items Here you change the maximum amount of entries that are displayed in the Combo Box (Drop Down List). |  |  |
| — | Drop Down Width | Here you change the width in pixel for the Combo Box (Drop Down List). |  |
| — | Text Border Style | Here you change the frame of the control: Fixed 3D3D frame Fixed SingleSingle frame NoneNo frame |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Settings |  |  |
| — | Right To Left | Here you set whether the content of the Combo Box should be displayed from left to right or from right to left. |  |
| — | Show Values | With this property, you specify whether to additionally display the decimal/hexadecimal value behind the symbolic value (in brackets). In this way, you recognize at a glance the "symbolic value - raw value" assignment. Here you can set the display to hexadecimal or binary format. |  |
| — | Sort Alphabetically | Here you select whether the entries are to be listed by name (alphabetical order) or by value. |  |
| — | Value Table | Here you select the value table from which the symbolic values are displayed. |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |
| Group: — | Symbol |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. Valid Data Types of Symbols |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |

## CAPL Access

With the function setControlProperty, you can set this property of the control.

Display Only

With a click on the symbol you switch between control and display element.

With activated option the control is used as display element.

—

Is Visible At Runtime

Specifies whether the control is to be displayed during runtime.

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

—

Tab Index

Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime.

Text Font / Combo Box Font Group

Font Text/Box

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

Appearance Group

Appearance

Combo Box Style

Here you change the list type:

Display Text

Here you change the alignment of the description:

Display Rows

Here you change the number of displayed items:

Drop Down Max Items

Number of Items

Here you change the maximum amount of entries that are displayed in the Combo Box (Drop Down List).

—

Drop Down Width

Here you change the width in pixel for the Combo Box (Drop Down List).

Text Border Style

Here you change the frame of the control:

More Group

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Settings

Right To Left

Here you set whether the content of the Combo Box should be displayed from left to right or from right to left.

Show Values

With this property, you specify whether to additionally display the decimal/hexadecimal value behind the symbolic value (in brackets). In this way, you recognize at a glance the "symbolic value - raw value" assignment.

Here you can set the display to hexadecimal or binary format.

Sort Alphabetically

Here you select whether the entries are to be listed by name (alphabetical order) or by value.

Value Table

Here you select the value table from which the symbolic values are displayed.

Layout

Location/Size

Here you can enter settings relating to the size and position of the control.

Note

You can also resize the control by dragging its markers.

Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel.

Symbol

You can assign a symbol to the control.

With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter.

Valid Data Types of Symbols

Symbol Filter

Here you select the type of the symbol you want to assign to your control.

Assigning Controls

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
