# Analog Gauge

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The Analog Gauge can be used as display element for symbol values within a defined value range. Ranges within the value range can be highlighted in color.

The following uses cases are possible with the Analog Gauge:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

Minimum and Maximum must be set in the Properties.

If Minimum/Maximum of the symbol are set in the database, these are applied automatically as the value range for the display scale. Otherwise, default values are assigned for the value range.

You can subdivide the value range into a maximum of three ranges, which are distinguished by color markings.

## Display Element

During runtime of CANoe/CANalyzer, the Analog Gauge indicates the current value of the symbol.

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
| Font Group | Font |  |  |
| Font | Font\|Name/Size | Here you change the font and the font size. |  |
| — | With a click on the symbol you increase the font size. |  |  |
| — | With a click on the symbol you reduce the font size. |  |  |
| Font\|Bold | With a click on the symbol you format the text bold. |  |  |
| Font\|Italic | With a click on the symbol you format the text italic. |  |  |
| Font\|Underline | With a click on the symbol you underline the text. |  |  |
| — | Font\|Strikeout | Here you strikeout the text. |  |
| — | Font\|Unit | Here you change the unit of the font size. |  |
| Text Color | Here you change the color of the text. CAPL Access The control can be activated with the following CAPL functions: With the function setControlForeColor, you can change the Text Color of the Analog Gauge. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Background Color | Here you change the background color of the text. CAPL Access The control can be activated with the following CAPL functions: With the function setControlBackColor, you can change the Background Color of the Analog Gauge. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |  |  |
| Appearance Group | Appearance |  |  |
| Text | Text | Here you change the description of the scale. |  |
| Minimum | Minimum | Here you change the minimum of the value range. |  |
| Maximum | Maximum | Here you change the maximum of the value range. |  |
| Scale Angle | Scale Angle | Here you change the scale angle. |  |
| Arrow Position | Arrow Position | Here you change the arrow position (start position). |  |
| — | Analog Gauge Style | Here you change the layout of the scale. |  |
| — | Border Style | Here you change the frame of the control: Fixed 3D3D frame Fixed SingleSingle frame NoneNo frame |  |
| — | Text Display | Here you can set whether the label of the scale should be displayed. |  |
| — | Value Display | Here you can set whether the values should be displayed on the scale. |  |
| Mean Range Group | Mean Range |  |  |
| Lower | Lower Range Limit | Here you set the limit of he lower range. The lower limit value could not be smaller than the minimum. |  |
| Upper | Upper Range Limit | Here you set the limit of the upper range. The upper limit value could not be higher than the maximum. |  |
| Ranges Group | Ranges |  |  |
| Lower | Lower Range Color | Here you change the color of the lower range. |  |
| Lower Range Display | With a click on the symbol you activate/deactivate the colored display of the lower range. |  |  |
| Mean | Mean Range Color | Here you change the color of the mean range. |  |
| Mean Range Display | With a click on the symbol you activate/deactivate the colored display of the mean range. |  |  |
| Upper | Upper Range Color | Here you change the color of the upper range. |  |
| Upper Range Display | With a click on the symbol you activate/deactivate the colored display of the upper range. |  |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Appearance Arrow | Here you can change width and color of the pointer and size and color of the scale center. |  |
| Group: — | Appearance Frame | Here you can enter settings relating to the frame. |  |
| Group: — | Appearance Ticks | Here you can change length, number and color of theticks. The number of ticks Main Ticks Number can only be changed if the automatic calculation Automatic Adjustment is deactivated. |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |
| Group: — | Symbol |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. See also Configuration of the control. Valid Data Types of Symbols |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

Font Group

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

The control can be activated with the following CAPL functions:

Background Color

Here you change the background color of the text.

## CAPL Access

The control can be activated with the following CAPL functions:

Appearance Group

Appearance

Text

Here you change the description of the scale.

Minimum

Here you change the minimum of the value range.

Maximum

Here you change the maximum of the value range.

Scale Angle

Here you change the scale angle.

Arrow Position

Here you change the arrow position (start position).

—

Analog Gauge Style

Here you change the layout of the scale.

Border Style

Here you change the frame of the control:

Text Display

Here you can set whether the label of the scale should be displayed.

Value Display

Here you can set whether the values should be displayed on the scale.

Mean Range Group

Mean Range

Lower

Lower Range Limit

Here you set the limit of he lower range.

The lower limit value could not be smaller than the minimum.

Upper

Upper Range Limit

Here you set the limit of the upper range.

The upper limit value could not be higher than the maximum.

Ranges Group

Ranges

Lower Range Color

Here you change the color of the lower range.

Lower Range Display

With a click on the symbol you activate/deactivate the colored display of the lower range.

Mean

Mean Range Color

Here you change the color of the mean range.

Mean Range Display

With a click on the symbol you activate/deactivate the colored display of the mean range.

Upper Range Color

Here you change the color of the upper range.

Upper Range Display

With a click on the symbol you activate/deactivate the colored display of the upper range.

More Group

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Appearance Arrow

Here you can change width and color of the pointer and size and color of the scale center.

Appearance Frame

Here you can enter settings relating to the frame.

Appearance Ticks

Here you can change length, number and color of theticks.

The number of ticks Main Ticks Number can only be changed if the automatic calculation Automatic Adjustment is deactivated.

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
