# LCD Control

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Cases

The LCD Control is used to display floating-point numbers. The individual digits have the appearance of an LCD display.

The following use cases are possible with the LCD Control:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

## Display Element

During runtime of CANalyzer the LCD Control indicates the current symbol value.

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
| Number of Digits Group | Number of Digits |  |  |
| Before Decimal Point | Before Decimal Point | Here you change the number of digits before the decimal point. Possible values: 0 – 20 If the number of digits before the decimal point exceeds the definition, the digits at the front are truncated. A triangle is displayed in the upper left corner of the element during runtime to indicate that not all digits have been displayed. If the number of digits before the decimal point is less than the definition, the extra digits are filled with zeros. CAPL Access With the function setControlProperty, you can set this property of the control. |  |
| After Decimal Point | After Decimal Point | Here you change the number of decimal places. Possible values: 0 – 20 If the number of decimal places exceeds the definition, the value is truncated after the defined number. Rounding does not take place.If the number of decimal places is less than the definition, the extra spaces are filled with zeros. CAPL Access With the function setControlProperty, you can set this property of the control. |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Appearance |  |  |
| — | Background Color | Here you change the background color of the LCD Control. CAPL Access With the function setControlBackColor, you can change the Background Color of the LCD Control. With the function setDefaultControlColors, you can reset the background colors to the default values defined in the Panel Designer. |  |
| — | Background Is Transparent | Allows the control background to show through. If the property is set to True, the Background Color property is grayed out and cannot be used. If the property is set to False, the element is displayed with the specified background color. |  |
| — | Segment Color Off | Here you change the color for switched-off segments. |  |
| — | Segment Color On | Here you change the color for segments that display the current number and are thereby switched on. |  |
| — | Segment Strength | Here you change the line thickness of the segments. |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |
| Group: — | Symbol |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. Valid Data Types of Symbols |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

Number of Digits Group

Number of Digits

Before Decimal Point

Here you change the number of digits before the decimal point.

Possible values: 0 – 20

If the number of digits before the decimal point exceeds the definition, the digits at the front are truncated. A triangle is displayed in the upper left corner of the element during runtime to indicate that not all digits have been displayed. If the number of digits before the decimal point is less than the definition, the extra digits are filled with zeros.

## CAPL Access

With the function setControlProperty, you can set this property of the control.

After Decimal Point

Here you change the number of decimal places.

Possible values: 0 – 20

If the number of decimal places exceeds the definition, the value is truncated after the defined number. Rounding does not take place.If the number of decimal places is less than the definition, the extra spaces are filled with zeros.

## CAPL Access

With the function setControlProperty, you can set this property of the control.

More Group

—

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Appearance

Background Color

Here you change the background color of the LCD Control.

## CAPL Access

—

Background Is Transparent

Allows the control background to show through.

If the property is set to True, the Background Color property is grayed out and cannot be used.

If the property is set to False, the element is displayed with the specified background color.

Segment Color Off

Here you change the color for switched-off segments.

Segment Color On

Here you change the color for segments that display the current number and are thereby switched on.

Segment Strength

Here you change the line thickness of the segments.

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

Valid Data Types of Symbols

Symbol Filter

Here you select the type of the symbol you want to assign to your control.

Assigning Controls

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
