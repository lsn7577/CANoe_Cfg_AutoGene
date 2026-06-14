# Clock Control

> Category: `Panel` | Subcategory: `Elements` | Type: `concept`

Note

| Note In CANalyzer fun, the Clock Control can only display the PC's system time (Mode = Clock, Source = PC System Time). Other use cases are not supported. If you open a panel in CANalyzer CANalyzer fun that has an existing Clock Control which is set to StopWatch mode, the Clock Control is disabled. |
|---|

## Use Case

The Clock Control element lets you display the time in digital form.

The following use cases are possible with the Clock Control:

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

The symbol is updated at runtime in the following way, depending on the data type selected and whether the 12-hour clock convention is used:

24h

hh:mm:ss

A[0] = hh

A[1] = mm

A[2] = ss

12h

hh:mm:ss AM

hh:mm:ss PM

A[3] = 0 for AM

A[3] = 1 for PM

Note

A[3] is updated for both the 24-hour and 12-hour display modes to prevent access errors from triggering a crash.

Note for Symbol Updates

If the panel is closed in CANoe at runtime, the time cannot be written to the corresponding symbol. In this case, the Clock Control and its symbolic link are not recognized in CANoe.

You can configure the control via the ribbon or the Properties Window.

Example: Displaying the PC's System Time

Example 2: Using a timer in CAPL and display it on the Clock Control

| Property'Display Style' | Data type'String' | Data type'Integer Array' |
|---|---|---|
| 24h | hh:mm:ss | A[0] = hh A[1] = mm A[2] = ss |
| 12h | hh:mm:ss AM hh:mm:ss PM | A[0] = hh A[1] = mm A[2] = ss A[3] = 0 for AM A[3] = 1 for PM |

| Note A[3] is updated for both the 24-hour and 12-hour display modes to prevent access errors from triggering a crash. |
|---|

| Note for Symbol Updates If the panel is closed in CANoe at runtime, the time cannot be written to the corresponding symbol. In this case, the Clock Control and its symbolic link are not recognized in CANoe. |
|---|

| Example: Displaying the PC's System Time To display the PC's system time, you need to set the Mode = Clock and Source = PCSystemTime properties in the Panel Designer. The PC's system time is shown as the time when measurement starts. The display is updated cyclically (every second). The current time is written to the symbol cyclically (every second). |
|---|

| Example 2: Using a timer in CAPL and display it on the Clock Control To display a timer that is programmed in CAPL, you need to set the Mode = Clock and Source = CAPL properties in the Panel Designer. In the CAPL code two timers are set: The first timer triggers a certain action after expiration, e.g. stopping a measurement. The second timer is used for the cyclic update in the Clock Control and must not be smaller that 1 second. CAPL Code variables{ // Timer Timer TimerTimer; //timer in s for timer functionality msTimer UpdatePanelTimer; //timer in ms to update the clock control on panel}on sysvar StartTimer{ setTimer(TimerTimer, 60); //set the timer to 60 seconds if the timer stops doing something setTimerCyclic(UpdatePanelTimer, 1000); //set the update of the timer (cyclic) for panel on 1000ms}on timer TimerTimer{ //do something: e.g. Stop Measurement cancelTimer(UpdatePanelTimer); //cancel the cyclic update timer}on timer UpdatePanelTimer{ //set the remaining time on clock control setClockControlTime("PanelName", "Clock Control Name", timeToElapse(TimerTimer));} |
|---|

### CAPL Code

```c
variables
{
// Timer
Timer TimerTimer; //timer in s for timer functionality
msTimer UpdatePanelTimer; //timer in ms to update the clock control on panel
}
on sysvar StartTimer
{
setTimer(TimerTimer, 60); //set the timer to 60 seconds if the timer stops doing something
setTimerCyclic(UpdatePanelTimer, 1000); //set the update of the timer (cyclic) for panel on 1000ms
}
on timer TimerTimer
{
//do something: e.g. Stop Measurement
cancelTimer(UpdatePanelTimer); //cancel the cyclic update timer
}
on timer UpdatePanelTimer
{
//set the remaining time on clock control
setClockControlTime("PanelName", "Clock Control Name", timeToElapse(TimerTimer));
}
```

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
| Settings Group | Settings |  |  |
| Mode | Here you change the usage: ClockIn this case, you also need to configure the Source property. Stop WatchThe stop watch always starts at zero. You cannot modify this start value. The clock is updated every second. CAPL Access (for clock only) In order to set the time using CAPL at a given point in time, you need to set the Mode = Clock and Source = CAPL properties in the Panel Designer. You can then use the setClockControlTime function to set the time. This function can display the time as: Hours, minutes, seconds or Seconds (converted to hours, minutes, seconds at runtime) The symbol is updated when the time is set in CAPL. CAPL Access (for stop watch only) To use the Clock Control as a stopwatch, you need to set the Mode = StopWatch property in the Panel Designer. The start time is always 00:00:00 or 00:00 (depending on the Display Seconds property setting) and cannot be changed. You use CAPL functions to start, stop and reset the stopwatch. The clockControlStart function starts the stopwatch. It is updated every second. clockControlStop stops the stopwatch. The currently displayed stop time remains visible; it is not automatically reset to zero. If you restart the clock, it will continue from this position. You can reset the clock (to the start time) using the clockControlReset function. The current time is only written to the symbol when the clock starts or stops. The cyclical updates that take place every second are not written to the symbol. Note The stopwatch runs from 00 to 99 o'clock and then starts again at 00 o'clock. You can only start and reset the stopwatch when it is not running. | Note The stopwatch runs from 00 to 99 o'clock and then starts again at 00 o'clock. You can only start and reset the stopwatch when it is not running. |  |
| Note The stopwatch runs from 00 to 99 o'clock and then starts again at 00 o'clock. You can only start and reset the stopwatch when it is not running. |  |  |  |
| Display Seconds | Display Seconds With a click on the symbol you change display. With activated option the time display includes seconds as well as hours and minutes. If you enable Display Seconds, the display shows hh:mm:ss. If you disable Display Seconds, the display shows hh:mm. |  |  |
| Style | Display Style | Here you change the time setting: 12h format, (i.e. a 12-hour clock with AM/PM) 24h format If you select the 12-hour clock format with AM/PM (Display Style = 12h) the display works as follows: 0 o'clock/24:00 is shown as 12:00 AM. 12:00 noon is shown as 12:00 PM. Note This property is disabled when Stop Watch mode is selected. | Note This property is disabled when Stop Watch mode is selected. |
| Note This property is disabled when Stop Watch mode is selected. |  |  |  |
| Source | Source | Here you change the source of the time: System TimeThe system time of the PC is used. CAPLThe time in the control is set via CAPL. Note This property is disabled when StopWatch mode is selected. | Note This property is disabled when StopWatch mode is selected. |
| Note This property is disabled when StopWatch mode is selected. |  |  |  |
| More Group | — |  |  |
| — | Show Properties With a click on the symbol you open the Properties Window. |  |  |
| Group: — | Appearance |  |  |
| — | Background Color | Here you change the background color of the Clock Control. CAPL Access You can use the setControlForeColor and setControlBackColor CAPL functions to modify the text and background color at runtime. The setDefaultControlColors CAPL function lets you reset the background colors to default values, which are defined in the Panel Designer. |  |
| — | Background Is Transparent | Makes it possible to see through the control's background. If you set this property to True, the Background Color property is disabled and is not used. If you set the property to False, the control is displayed using the specified background color. |  |
| — | Segment Color Off | Here you change the color for segments that are switched off. |  |
| — | Segment Color On | Here you change the color for segments that show the current time (and are thus switched on). |  |
| — | Segment Strength | Here you change the line point size for the segments. |  |
| Group: — | Layout |  |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  |  |  |
| Group: — | Symbol |  |  |
| — | Symbol | You can assign a symbol to the control. With a click on [...] you open the Symbol Selection dialog. Note your setting in Symbol filter. Valid Data Types of Symbols |  |
| — | Symbol Filter | Here you select the type of the symbol you want to assign to your control. |  |

## CAPL Access

With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

Settings Group

Settings

Mode

Here you change the usage:

## CAPL Access (for clock only)

## CAPL Access (for stop watch only)

To use the Clock Control as a stopwatch, you need to set the Mode = StopWatch property in the Panel Designer.

Note

Display Seconds

With a click on the symbol you change display.

With activated option the time display includes seconds as well as hours and minutes.

Style

Display Style

Here you change the time setting:

If you select the 12-hour clock format with AM/PM (Display Style = 12h) the display works as follows:

This property is disabled when Stop Watch mode is selected.

Source

Here you change the source of the time:

This property is disabled when StopWatch mode is selected.

More Group

—

Show Properties

With a click on the symbol you open the Properties Window.

Group: —

Appearance

Background Color

Here you change the background color of the Clock Control.

| Note The stopwatch runs from 00 to 99 o'clock and then starts again at 00 o'clock. You can only start and reset the stopwatch when it is not running. |
|---|

| Note This property is disabled when Stop Watch mode is selected. |
|---|

| Note This property is disabled when StopWatch mode is selected. |
|---|

## CAPL Access

—

Background Is Transparent

Makes it possible to see through the control's background.

If you set this property to True, the Background Color property is disabled and is not used.

If you set the property to False, the control is displayed using the specified background color.

Segment Color Off

Here you change the color for segments that are switched off.

Segment Color On

Here you change the color for segments that show the current time (and are thus switched on).

Segment Strength

Here you change the line point size for the segments.

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

Assigning Controls | Clock Control and panel conversion

| Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|---|
