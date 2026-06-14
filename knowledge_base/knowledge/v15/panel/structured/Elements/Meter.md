# Meter

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

## Use Case

The Meter can be used as display element for values within a defined value range. Segments within the value range can be highlighted using a different pointer color.

The following use cases are possible with the Meter:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

You can configure the control via the ribbon or the Properties Window.

Minimum and Maximum must be set in the Properties.

If Minimum/Maximum of the symbol are set in the database, these are applied automatically as the value range for the display scale. Otherwise, default values are assigned for the value range.

You can position an image behind the Meter, e.g., to give it the appearance of a tachometer.

## Display Element

During runtime of CANalyzer, the Meter indicates the current value of the symbol.

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
| Aperture Angle Group | Aperture Angle |  |  |
| From | From | Here you change the opening angle of the Meter. A pointer pointing straight up corresponds to 0 degrees. |  |
| To | To |  |  |
| Value Range Group | Value Range |  |  |
| Minimum | Minimum | Here you change the minimum value of the value range of the opening angle |  |
| Maximum | Maximum | Here you change the maximum value of the value range of the opening angle |  |
| Needle Group | Appearance Needle |  |  |
| Shape | Here you change the form of the needle. |  |  |
| Needle Color | Color | Here you change the color of the needle. |  |
| Pivot Distance % | Pivot Distance | Here you change the length of the pointer past the pivot point (percent value of the extending part of the needle over its total length). |  |
| Alarm Group | Alarm Settings |  |  |
| Alarm Display | With a click on the symbol you switch on/off the display of the overshot/undershot of a defined value range. |  |  |
| Lower | Lower Limit/Lower Limit Color | Here you change the lower alarm limit value which, when undershot, triggers a reaction by the meter the color of the pointer when a set limit value is undershot If the value of the assigned symbol moves back into the range between the upper and lower limit values, the pointer once again takes on the color specified under Needle Color. |  |
| Upper | Upper Limit/Upper Limit Color | Here you change the upper alarm limit value which, when overshot, triggers a reaction by the meter the color of the pointer when a set limit value is overshot If the value of the assigned symbol moves back into the range between the upper and lower limit values, the pointer once again takes on the color specified under Needle Color. |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |
| Group: — | Symbol |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. Valid Data Types of Symbols |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

Aperture Angle Group

Aperture Angle

From

Here you change the opening angle of the Meter. A pointer pointing straight up corresponds to 0 degrees.

To

Value Range Group

Value Range

Minimum

Here you change the minimum value of the value range of the opening angle

Maximum

Here you change the maximum value of the value range of the opening angle

Needle Group

Appearance Needle

Shape

Here you change the form of the needle.

Needle Color

Color

Here you change the color of the needle.

Pivot Distance %

Pivot Distance

Here you change the length of the pointer past the pivot point (percent value of the extending part of the needle over its total length).

Alarm Group

Alarm Settings

Alarm Display

With a click on the symbol you switch on/off the display of the overshot/undershot of a defined value range.

Lower

Lower Limit/Lower Limit Color

Here you change

If the value of the assigned symbol moves back into the range between the upper and lower limit values, the pointer once again takes on the color specified under Needle Color.

Upper

Upper Limit/Upper Limit Color

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

Valid Data Types of Symbols

Symbol Filter

Here you select the type of the symbol you want to assign to your control.

Assigning Controls

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
