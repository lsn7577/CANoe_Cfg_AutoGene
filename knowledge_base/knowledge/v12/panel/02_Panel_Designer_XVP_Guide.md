# Panel Designer .xvp 面板文件编写指南 (Vector CANoe 12.0)

> 本文档基于 Vector CANoe 12.0 Panel Designer 帮助文档整理，涵盖 .xvp (extended Vector Panel) 面板文件的编写方法、控件使用、属性配置及 CAPL 接口。
> 适用对象：Panel 设计师、CANoe UI 开发工程师、HMI 测试工程师。
> 生成日期：2026/06/01
> 注: CANoe 12.0 Panel Designer 共支持 37 种控件。

---

## Panel Designer 概述


# Panel Designer

Start Page

| Screenshot | Quick Access |
| --- | --- |
|  | New Features Controls CAPL Functions Restricted Mode Compatibility |
| Overview of Program Functions | Brief Overview for New Users |
| Overview Functions of the program Description of the windows Window management Controls Control and display elements Symbols Transparency Color Procedures Opening the Panel Designer Creating a new panel Assigning controls Aligning controls Assigning symbols (drag and drop) Displaying assigned symbols Multiselection of controls Assigning and creating bitmaps Ribbon Ribbon Menu -> Ribbon | Functions of the program Screen format Window management Panel Designer / Panel Editor Convert panels |
| Tips & Tricks | Note |
| Aligning controls Status bar Keyboard operations context menu Displaying assigned symbols in CANoe/CANalyzer Displaying and entering hexadecimal or binary values Transparency Color Multiselection of controls Panel Conversion: Notes | Starting from version 7.0 you can easily design and configure panels (*.xvp) with the Panel Designer.Panels (*.cnp) which already exist will still be opened and edited in the Panel Editor. Signals, environment variables and system variables are called symbols. |

Contact/Copyright/License

| Version 12.0© Vector Informatik GmbH |  |


---

## Panel Designer 新特性 (CANoe 12.0)

### PanelDesignerNewFeatures


# New Features

Panel Designer » New Features

## Version 12.0

- Improved performance when copying and pasting within the Panel Designers.

- Improved loading times for configurations with many panels.

- For the LED Control the symbol value can be interpreted as RGB and the LED control can therefore be colored accordingly.

## Version 11.0 SP3

- Input/Output Box If the text is too long, you can select in the Properties Window whether the start of the text or the end of the text should be displayed.

- The Text and Control function on the Home ribbon tab aligns controls (Input/Output Box, Combo Box, Check Box, Radio Button) and adjusts the width of the label and element.

- Working with Value Tables You can assign switch values from value tables for the Button, Check Box, LED Control, Media Player, Radio Button, and Switch/Indicator controls.

## Version 11.0

- Picture Box To shorten the loading times of an image, you can now select in the Properties Window whether an image should be kept in cache memory or not.

- Switch/Indicator During a state change, besides concrete values, you can also enter value ranges to map, for example a digital fuel indicator.

- Panel Overview The new window lists controls which are integrated into the currently selected panel. In the tabular overview, you can

- quickly identify which symbols are assigned to which controls

- assign symbols to the controls

- find controls which are hidden or located outside the panel

## Version 10.0 SP4

- The new Method Call Control is used to send a function/method. You can set parameters and receive the corresponding return value.

## Version 10.0 SP3

- New setting Epsilon for the controls Check Box, LED Control, Radio Button and Switch/Indicator.By using this property, you will be able to set in the Panel Designer a value for the tolerated deviation of rounding inaccuracies.

- With the Clinometer you can display the transverse and longitudinal slopes.

## Version 10.0

- Ribbon Improved usa

[...truncated for brevity...]

---

## Panel 控件详细参考 (37 个)

### 控件: 


# Control and Display Elements

Panel Designer » Control and Display Elements

The following control types are differentiated:

| Control Type | Supported Symbols | Program Variants |
| --- | --- | --- |
| Display Element With display elements value changes of assigned symbols can be displayed. | Signals Diagnostics parameters Diagnostic DTC parameters System variables Environment variables | CANoe pex/pro CANoe run |
| Signals Diagnostics parameters Diagnostic DTC parameters System variables | CANalyzer pro/exp |
| Signals | CANalyzer fun |
| Control Element With control elements values of assigned symbols can be changed. | Signals System variables Environment variables | CANoe pex/pro |
| System variables | CANalyzer pro/exp |
| Static Element Static elements are used for graphic representation or explanatory purposes.No symbols can be assigned to them: | — | CANoe pex/pro CANoe run CANalyzer pro/exp CANalyzer fun |
| Special Element With special elements predefined actions can be performed. No symbols are assigned to them: File Button MOST Send Button Panel Control Button Start Stop Control | — | CANoe pro CANalyzer pro/exp |

|  | Note Many controls can be utilized as both control and display elements. In CANoe run and CANalyzer fun only display elements can be created and configured. Combined control and display elements can only be used as display element. |

Restricted Mode

| Version 12.0© Vector Informatik GmbH |  |


### 控件: AnalogGauge


# Analog Gauge

Panel Designer » Windows » Toolbox » Analog Gauge

## Use Case

The Analog Gauge can be used as display element for symbol values within a defined value range. Ranges within the value range can be highlighted in color.

The following uses cases are possible with the Analog Gauge:

- Display of the vehicle speed

- Display of the engine speed

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

Minimum and Maximum must be set in the Properties.

If Minimum/Maximum of the symbol are set in the database, these are applied automatically as the value range for the display scale. Otherwise, default values are assigned for the value range.

You can subdivide the value range into a maximum of three ranges, which are distinguished by color markings.

## Display Element

During runtime of CANoe/CANalyzer, the Analog Gauge indicates the current value of the symbol.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| Font Group | Font |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you reduce the font size. |
|  | Font|Bold | With a click on the symbol you format the text bold. |
|  | Font|Italic | With a click on the symbol you format the text italic. |
|  | Font|Underline | With a click on the symbol you underline the text. |
| — | Font|Strikeout | Here you strikeout the text. |
| — | Font|Unit | Here you change the unit of the font size. |
|  | Text Color | Here you change the color of the text. CAPL Access The

[...truncated for brevity...]

### 控件: Button


# Button

Panel Designer » Windows » Toolbox » Button

## Use Case

The Button is a control with which assigned actions can be triggered.

The following uses cases are possible with the Button:

- Pressing the Start button causes the motor to start.

- All of the vehicle doors are locked automatically when the Lock switch is actuated.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

## Control Element

If you click the Button during runtime of CANoe/CANalyzer, the value that you set in the Pressed property will be assigned to the symbol. Setting this value causes a stored action to be triggered.If you release the Button, the symbol receives the value that you have set in the Released property. This symbol value can also be used to trigger an action.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| Text | Text | Here you change the description of the control. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Font Group | Font |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you reduce the font size. |
|  | Font|Bold | With a click on the symbol you format the text bold. |
|  | Font|Italic | With a click on the symbol you format the text italic. |
|  | Font|Underline | With a click on the symbol you underline the text. |
| — | Font|Strikeout | Here you strikeout the text. |
| — | Font|Unit | Here you change the unit of the font s

[...truncated for brevity...]

### 控件: CAPLOutputView


# CAPL Output View

Panel Designer » Windows » Toolbox » CAPL Output View

|  | Note The CAPL Output View is not available in CANalyzer fun. |

## Use Case

The CAPL Output View is used to output text information from CAPL at runtime.

The following uses cases are possible with the CAPL Output View:

- Multi-line output of information during a test sequence.

- A signal value is not set correctly. A message is output in the CAPL Output View as a result of this error. To highlight the message compared to other text, it is output in red.

## Configuration

You cannot assign a symbol to the control because it is solely text output and is controlled only via CAPL.

You can configure the control via the ribbon or the Properties Window.

|  | Example You can carry out the following actions at runtime and/or after measurement stops. Action Keyboard Operations Element Context Menu Description Select text left mouse key — You can select a given text segment with the mouse. Pause/Resume None — If you move the scroll bar at the right edge of the CAPL Output View element upward during runtime, output into the element is paused. This allows you to view the currently visible text as long as you want.When you move the scroll bar down to the bottom end again, output to the CAPL Output View element resumes and the most recently output text appears. Copy <Ctrl>+<C> • You can copy selected text segments, including the text and background colors. Delete all <Del> • Deletes everything in the CAPL Output View element.It is not possible to delete individual segments. Select all <Ctrl>+<A> • Selects everything in the CAPL Output View element. | Action | Keyboard Operations | Element Context Menu | Description | Select text | left mouse key | — | You can select a given text segment with the mouse. | Pause/Resume | None | — | If you move the scroll bar at the right edge of the CAPL Output View element upward during runtime, output into the element is paused. This allows you to view the currently visible text as long as you want.When you move the scroll bar down to the bottom end again, output to the CAPL Output View element resumes and the most recently output text appears. | Copy | <Ctrl>+<C> | • | You can copy selected text segments, including the text and background colors. | Delete all | <Del> | • | Deletes everything in the CAPL Output View element.It is not possible to delete individual segments. | Select all | <Ctrl>+<A> | • | Selects everything in the CAPL Output View elem

[...truncated for brevity...]

### 控件: CheckBox


# Check Box

Panel Designer » Windows » Toolbox » Check Box

## Use Case

The Check Box can be used as a control and display element, with which an option can be initiated or displayed.

The following uses cases are possible with the Check Box:

- Simulation of an error during the test sequence should be possible. If the Check Box is activated, the error scenario will be triggered.

- Sets a signal to a particular value.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

## Control Element

If you activate the Check Box during runtime of CANoe/CANalyzer, the value that you set in the Switch Value 'Checked' property in the Settings category will be assigned to the symbol. Setting this value causes a stored action to be triggered.

If you deactivate the Check Box, the symbol receives the value that you have set in the Switch Value 'Unchecked' property. This symbol value can also be used to trigger an action.

## Display Element

The symbol is not set manually. Rather it is set to the Switch Value 'Checked' or Switch Value 'Unchecked' values by simulation or CAPL programs, for example. The Check Box responds accordingly, e.g., by appearing to be activated.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| Text | Text | Here you change the description of the control. |
|  | Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab 

[...truncated for brevity...]

### 控件: Clinometer


# Clinometer

Panel Designer » Windows » Toolbox » Clinometer

## Use Cases

The Clinometer displays the transverse and the longitudinal slopes (roll and pitch). You can select one of the following views and functions:

- Transverse slope of a vehicle

- Longitudinal slope of a vehicle

- Transverse slope of a airplane

- Longitudinal slope of a airplane

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

The view only displays the transverse slope or the longitudinal slope. No combined view is available. The value can be read on the scale in the image or displayed as a number below the image.

You can configure the control via the ribbon or the Properties Window.

## Display Element

During runtime of CANoe/CANalyzer the Clinometer indicates the current symbol value.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| View Group | Clinometer Settings |  |
|  | View | Here you can change the view and the type of the display: Vehicle: PitchLongitudinal slope of a vehicle Vehicle: RollTransverse slope of a vehicle Airplane: PitchDescent and climb of a airplane Airplane: RollTurning flight of a airplane |
| Value Group | Clinometer Settings |  |
|  | Show Value | Show With a click on the symbol you switch on or off the display of the slope below the image. |
|  | Show Decimal Places | Decimal Place With a click on the symbol the slope value below the image is displayed with or without a decimal. |
| Value Font Group | Font |  |
| Font | Value Font | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you reduce the font size

[...truncated for brevity...]

### 控件: ClockControl


# Clock Control

Panel Designer » Windows » Toolbox » Clock Control

|  | Note In CANalyzer fun, the Clock Control can only display the PC's system time (Mode = Clock, Source = PC System Time). Other use cases are not supported. If you open a panel in CANalyzer fun that has an existing Clock Control which is set to StopWatch mode, the Clock Control is disabled. |

## Use Case

The Clock Control element lets you display the time in digital form.

The following use cases are possible with the Clock Control:

- Display of the PC's system time (PC time).

- Transmission of the time from CAPL to the Clock Control at runtime.

- Use as a stopwatch.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

The symbol is updated at runtime in the following way, depending on the data type selected and whether the 12-hour clock convention is used:

| Property'Display Style' | Data type'String' | Data type'Integer Array' |
| --- | --- | --- |
| 24h | hh:mm:ss | A[0] = hh A[1] = mm A[2] = ss |
| 12h | hh:mm:ss AM hh:mm:ss PM | A[0] = hh A[1] = mm A[2] = ss A[3] = 0 for AM A[3] = 1 for PM |

|  | Note A[3] is updated for both the 24-hour and 12-hour display modes to prevent access errors from triggering a crash. |

|  | Note for Symbol Updates If the panel is closed in CANoe at runtime, the time cannot be written to the corresponding symbol. In this case, the Clock Control and its symbolic link are not recognized in CANoe. |

You can configure the control via the ribbon or the Properties Window.

|  | Example: Displaying the PC's System Time To display the PC's system time, you need to set the Mode = Clock and Source = PCSystemTime properties in the Panel Designer. The PC's system time is shown as the time when measurement starts. The display is updated cyclically (every second). The current time is written to the symbol cyclically (every second). |

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and t

[...truncated for brevity...]

### 控件: ComboBox


# Combo Box

Panel Designer » Windows » Toolbox » Combo Box

## Use Case

The Combo Box can be used as a control and display element for selecting or displaying symbolic values from value tables of a database or system variable definition.

The following use cases are possible with the Combo Box:

- Sets the ignition lock to the Lock, Off, On, or Start status.

- Sets the hand brake statuses.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

Assign a symbol to the Combo Box in the Panel Designer.A value table with symbolic values must be assigned to the symbol so that the symbolic values can be selected and displayed during runtime of CANoe/CANalyzer.

You can configure the control via the ribbon or the Properties Window.

## Control Element

During runtime of CANoe/CANalyzer you can select a symbolic value in the Combo Box that is assigned to the symbol.

## Display Element

The symbol value is not set manually. Rather it is set by simulation or CAPL programs, for example. The Combo Box displays the symbolic value automatically.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| Text | Text | Here you change the description of the control. |
|  | Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Text Font / Combo Box Font Group | Font Text/Box |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increas

[...truncated for brevity...]

### 控件: Compass


# Compass

Panel Designer » Windows » Toolbox » Compass

## Use Cases

The Compass is used to display the cardinal points and the speed.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

The compass is composed of two controls. Therefore assign a symbol to the display of the cardinal points (Direction) and the display of the speed (Speed) in the Panel Designer.

If you assign one or several symbols to the compass using drag and drop or via the context menu, the Assign Symbols dialog is opened in which you can assign the symbols to the two controls on the compass (Direction and Speed). On the left side of the dialog, you can see all symbols which you have assigned to the compass. You can assign these symbols to the controls on the right side using drag and drop. Symbols which are already assigned to one of the two controls, are marked with .

Use to remove an already assigned symbol.

|  | Note If you drag a system variable of the type GPS::GPSData on the panel, a compass is automatically inserted and linked to the structure members Direction and Speed. If you drag a system variable of the type GPS::GPSData on a compass, the structure members Direction and Speed are automatically linked to the corresponding controls on the compass. If you drag symbols with the name Direction and Speed on a compass, they are automatically linked to the corresponding controls on the compass. |

If you want to remove a symbol assignment via the context menu command Detach Selected Symbols, a dialog opens in which you can select one or all assignments using .

You can configure the control via the ribbon or the Properties Window.

## Display Element

During runtime of CANoe/CANalyzer the Compass indicates the current symbol value.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to

[...truncated for brevity...]

### 控件: DataTypes


# Data Types of Assigned Symbols

Panel Designer » Toolbox » Data Types of Assigned Symbols

In the following table you can find an overview about valid data types of assigned symbols:

| Control | Integer/Long | Float/Double | String | Integer/Long Array | Byte Array (Data) | Non |
| --- | --- | --- | --- | --- | --- | --- |
| Analog Gauge | ● | ● | — | — | — | — |
| Button | ● | ● | — | — | — | — |
| CAPL Output View | — | — | — | — | — | ● |
| Check Box | ● | ● | — | — | — | — |
| Clinometer | ● | ● | — | — | — | — |
| Clock Control | — | — | ● | ● | — | — |
| Combo Box | ● | — | — | — | — | — |
| Compass (Direction/Speed) | ● | ● | — | — | — | — |
| File Button | — | — | — | — | — | ● |
| Group Box | — | — | — | — | — | ● |
| Hex/Text Editor | — | — | ● | ● | ● |  |
| Input/Output Box | ● | ● | ● | — | — | — |
| LCD Control | ● | ● | — | — | — | — |
| LED Band | ● | ● | — | — | ● | — |
| LED Control | ● | ● | — | — | — | — |
| Media Player | ● | ● | — | — | — | — |
| Media Stream Control |  |  | — | — | — | ● |
| Meter | ● | ● | — | — | — | — |
| MOST Send Button | — | — | — | — | — | ● |
| NM Control | — | — | — | — | — | ● |
| Numeric Up/Down | ● | ● | — | — | — | — |
| Panel Control Button | — | — | — | — | — | ● |
| Path Dialog | — | — | ● | — | — |  |
| Picture Box | — | — | — | — | — | ● |
| Progress Bar | ● | ● | — | — | — | — |
| Radio Button | ● | ● | — | — | — | — |
| Start Stop Control | — | — | — | — | — | ● |
| Static Text | — | — | — | — | — | ● |
| Switch/Indicator | ● | ● | — | — | — | — |
| Tab Control | ● | — | — | — | — | — |
| Track Bar | ● | ● | — | — | — | — |
| User-defined Controls(derived from PluginPanelControl) | ● | ● | — | — | — | — |

Assigning Symbols

| Version 12.0© Vector Informatik GmbH |  |


### 控件: GroupBox


# Group Box

Panel Designer » Windows » Toolbox » Group Box

## Use Case

The Group Box is a static element and serves to combine multiple elements.

The following use cases are possible with the Group Box:

- The four ignition statuses are represented by four options. These are grouped in a group box.

- All signals of a message are grouped in a group box.

## Configuration

Drag the relevant controls to the Group Box in the Panel Designer. The font type and size of the Group Box is assigned automatically to the controls.

Use the snaplines that appear to arrange the controls as required.

|  | Note When you move the Group Box, all the controls inside it will move too, but this will not affect how they are arranged within the box. |

You can configure the control via the ribbon or the Properties Window.

The Group Box and the elements it contains are displayed during runtime of CANoe/CANalyzer.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| Text | Text | Here you change the description of the control. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Font Group | Font |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you reduce the font size. |
|  | Font|Bold | With a click on the symbol you format the text bold. |
|  | Font|Italic | With a click on the symbol you format the text italic. |
|  | Font|Underline | With a click on the symbol you underline the text. |
| — | Font|Strikeout | Here you strikeout the text. |
| — | Font|Unit | Here you change the unit of the font size. |
|  | Text Color | Here you change the color of the text. |
|  | Background Color | Here you change the background color of the text. |
| More Group | — |  |
|  | — | Show Properties With a click on the symbol you open the Properties Wi

[...truncated for brevity...]

### 控件: HexTextEditor


# Hex/Text Editor

Panel Designer » Windows » Toolbox » Hex/Text Editor

## Use Case

The Hex/Text Editor can be used as a control and display element for inputting and displaying larger quantities of data.

In the Hex/Text Editor Ascii characters or decimal values can be displayed in hex format.

The following use cases are possible with the Hex/Text Editor:

- Display of data bytes in hex format

- Display of data bytes in decimal format

- Display of integer arrays in hex format

- Display of integer arrays in decimal format

- Use as text output

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

## Control Element

During runtime of CANoe/CANalyzer, you can enter text/hexadecimal values in the Hex/Text Editor.

## Display Element

The symbol value is not set manually. Rather it is set by simulation or CAPL programs, for example. The Hex/Text Editor displays the symbol value automatically.

|  | Note If the Text field is read only, values cannot be copied from it. |

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
|  | Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Font Group | Font |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you reduce the font size. |
|  | 

[...truncated for brevity...]

### 控件: InputOutputBox


# Input/Output Box

Panel Designer » Windows » Toolbox » Input/Output Box

## Use Case

The Input/Output Box can be used as a control and display element for inputting and outputting symbol values.

The following use cases are possible with the Input/Output Box:

- Display of wheel speed

- Sets the vehicle speed to a particular value.

- When the engine speed of 3000 revolutions per minute is exceeded, the Input/Output Box turns red.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

You can assign a color for the box background and/or box text to highlight a violation the valid signal value range (value range is exceeded or fallen below).

## Control Element

You can enter a value in the field during runtime of CANoe/CANalyzer. This value is assigned to the symbol.

## Display Element

The symbol value is not set manually. Rather it is set by simulation or CAPL programs, for example. The Input/Output Box displays the symbol value automatically.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| Text | Text | Here you change the description of the control. |
|  | Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Text Font / Text Box Font Group | Font Text/Box |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size

[...truncated for brevity...]

### 控件: LCDControl


# LCD Control

Panel Designer » Windows » Toolbox » LCD Control

## Use Cases

The LCD Control is used to display floating-point numbers. The individual digits have the appearance of an LCD display.

The following use cases are possible with the LCD Control:

- Display of vehicle speed

- Display of motor speed

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

## Display Element

During runtime of CANoe/CANalyzer the LCD Control indicates the current symbol value.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| Number of Digits Group | Number of Digits |  |
| Before Decimal Point | Before Decimal Point | Here you change the number of digits before the decimal point. Possible values: 0 – 20 If the number of digits before the decimal point exceeds the definition, the digits at the front are truncated. A triangle is displayed in the upper left corner of the element during runtime to indicate that not all digits have been displayed. If the number of digits before the decimal point is less than the definition, the extra digits are filled with zeros. |
| After Decimal Point | After Decimal Point | Here you change the number of decimal places. Possible values: 0 – 20 If the number of decimal places exceeds the definition, the value is truncated after the defined number. Rounding does not take place.If the number of decimal places is less than the definition, the extra spaces are filled with zeros. |
| More Group | — |  |
|  | — | Show Properties With a click on the symbol you open the Properties Window. |
| Group: — | Appearance |  |
| — | Backgr

[...truncated for brevity...]

### 控件: LED


# LED Control

Panel Designer » Windows » Toolbox » LED Control

## Use Cases

The LED Control can be used as a control and display element for selecting and displaying of two defined states (LED on/LED off). The individual statuses are shown graphically.

The following use cases are possible with the LED Control:

- Switching on and switching off a lamp

- Indicates that a particular state is reached

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

## Control Element

During runtime of CANoe/CANalyzer, you can actuate the LED Control; the corresponding symbol value is assigned to the symbol and the LED Control displays the associated state.

## Display Element

The symbol is not set manually to a defined condition. Rather it is set by simulation or CAPL programs, for example. The LED Control displays the associated state.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
|  | Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Switch Values Group | Switch Values |  |
| On | On LED Color On Value | Here you change the symbol value and the color for the switched on LED Control. If the assigned symbol is linked to a value table, you can assign a value from the value table to the switch value. CAPL Access With the function setControlForeColor, you can change the LED Color On of the LED Control. |
| Of

[...truncated for brevity...]

### 控件: LEDBand


# LED Band

Panel Designer » Windows » Toolbox » LED Band

## Use Cases

The LED Band is a display element to highlight areas on a panel for a defined state.

The following use cases are possible with the LED Band:

- Highlighting a defined area in a special color.

- To display the different interior lightning settings within a vehicle.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

## Display Element

During runtime of CANoe/CANalyzer the symbol value is interpreted as a color value including transparency level. The LED Band is displayed in the indicated color and the indicated transparency.

## Changing the LED Band with the Mouse

Select the LED Band and move the mouse over the displayed image. The following white selection points are then displayed.

Use the two outer points to move the endpoints of the LED Band and thus change the properties

- Location

- LED Band Length

- Rotation

- Size

Use the middle point to change the height of the LED Band and thus change the properties

- Location

- LED Band Height

- Size

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| Appearance Group | Appearance |  |  |
| Length | LED Band Length | Here you change the length of the LED Band |
| Height | LED Band Height | Here you change the height of the LED Band |
| Rotation | Rotation | Here you change the rotation angle of the LED Band. Rotation range -180° bis +180° Example: |
|  | Round Corners | Here you change the rounding of the corners: RoundLED Band with rounded corners SquareLED Band without rounded corners |
|  | Fade Color | Here yo

[...truncated for brevity...]

### 控件: MOSTSendButton


# MOST Send Button

Panel Designer » Windows » Toolbox » MOST Send Button

## Use Case

The MOST Send Button is a control with which assigned MOST messages can be sent on a specified channels.

## Configuration

You can configure the control via the ribbon or the Properties Window.

## Control Element

If you click the MOST Send Button during runtime of ,CANoe/CANalyzer the defined messages are sent to the corresponding channel at the specified sending interval.

In addition, you can specify whether a waiting period for the receipt confirmation is to be set and, if so, the length of the waiting period.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| Text | Text | Here you change the description of the control. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Font Group | Font |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you reduce the font size. |
|  | Font|Bold | With a click on the symbol you format the text bold. |
|  | Font|Italic | With a click on the symbol you format the text italic. |
|  | Font|Underline | With a click on the symbol you underline the text. |
| — | Font|Strikeout | Here you strikeout the text. |
| — | Font|Unit | Here you change the unit of the font size. |
|  | Text Color | Here you change the color of the text. |
|  | Background Color | Here you change the background color of the text. |
|  | Text Align | With a click on the symbol you align the text on the left site of the control. |
|  | Text Align | With a click on the symbol you align the text in the middle of the control. |
|  | Text Align | With a click on the symbol you align the text on the right site of the control. |
| Send Settings Group | Settings |  |
|  | Wait for Ack | Wait for Ack With a click on the symbol you ac

[...truncated for brevity...]

### 控件: MediaPlayer


# Media Player

Panel Designer » Windows » Toolbox » Media Player

## Use Cases

The Media Player is used to play media files (audio files, videos, etc.).

The following use cases are possible with the Media Player:

- Plays operating manuals in media formats.

- Stores defined events with signal tones.

## Configuration

|  | Note The Vector Media Player uses the Windows Media Player. A codec is expected for special files (e.g., AVI). If this is not present, an attempt is made to establish an Internet connection in order to find and install the missing codec. To prevent this, the File|Work Offline setting must be selected in the Windows Media Player. If a required codec is not present, the file will be played but an image will not appear or the preset visualization will be shown. The sound is reproduced. An error provider in the Vector Media Player references the missing codec. To be certain that the file can be played, you should play it in Windows Media Player in advance. |

You can use the assigned symbol to play, stop, and pause the selected media file. The individual statuses are defined using the Play, Stop, and Pause symbol values.

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

Depending on the configuration you can also operate the Media Player using a displayed toolbar. This has no effect on the linked symbol.

The defined symbol value for Play is checked at the measurement start. If the defined value is reached, the selected media file is played. The media file is stopped at the measurement end.

If a change is made to another desktop, a media file that is currently being played will be stopped automatically.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL

[...truncated for brevity...]

### 控件: MediaStream


# Media Stream Control

Panel Designer » Windows » Toolbox » Media Player

## Use Cases

The Media Stream Control is used to play streaming media received from the network (audio and video).

The following use cases are possible with the Media Stream Control:

- Display of a camera image of an in-network camera.

- Playing of a tone sequence from an audio stream of an on-board computer.

- Integrate video/audio sequences in a dashboard that is represented by a panel.

## Configuration

The capability of the control to render streaming media depends on the format of the streaming content on the network and the availability of a codec used for decoding this streaming content.

The following network protocols are supported:

- MAC Layer: AVTP Protocols according to IEEE 1722

- AAF (AVTP Audio Format)

- CVF (Compressed Video Format), Content: H.264 and MJPEG

- IP Layer: RTP Encodings (RFC 3550, IEEE 1733)

- L16 (Uncompressed Audio, RFC 3551)

- H.264 (Video, RFC 6184)

## Ribbon|Properties Tab

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| More Group | — |  |
|  | — | Show Properties With a click on the symbol you open the Properties Window. |
| Group: — | Appearance |  |
| — | Border Style | Here you change the frame of the control: Fixed 3D3D frame Fixed SingleSingle frame NoneNo frame |
| — | Media Streams | Here, you configure the network media streams that should be played. Once the stream with the configured Stream ID is received during the measurement it is automatically played. |

Assigning Controls

| Version 12.0© Vector Informatik GmbH |  |


### 控件: Meter


# Meter

Panel Designer » Windows » Toolbox » Meter

## Use Case

The Meter can be used as display element for values within a defined value range. Segments within the value range can be highlighted using a different pointer color.

The following use cases are possible with the Meter:

- Display of vehicle speed

- Display of engine speed

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

Minimum and Maximum must be set in the Properties.

If Minimum/Maximum of the symbol are set in the database, these are applied automatically as the value range for the display scale. Otherwise, default values are assigned for the value range.

You can position an image behind the Meter, e.g., to give it the appearance of a tachometer.

## Display Element

During runtime of CANoe/CANalyzer, the Meter indicates the current value of the symbol.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| Aperture Angle Group | Aperture Angle |  |
| From | From | Here you change the opening angle of the Meter. A pointer pointing straight up corresponds to 0 degrees. |
| To | To |
| Value Range Group | Value Range |  |
| Minimum | Minimum | Here you change the minimum value of the value range of the opening angle |
| Maximum | Maximum | Here you change the maximum value of the value range of the opening angle |
| Needle Group | Appearance Needle |  |
|  | Shape | Here you change the form of the needle. |
| Needle Color | Color | Here you change the color of the needle. |
| Pivot Distance % | Pivot Distance | Here you change the length of the pointer past the pivot point (p

[...truncated for brevity...]

### 控件: MethodCall


# Method Call Control

Panel Designer » Windows » Toolbox » Method Call Control

## Use Case

|  | Note Only available if the Panel Designer was opened from CANoe/CANalyzer and a configuration with communication objects (service-oriented communication) is loaded there. |

The Method Call Control is used to call a function/method. You can set parameters and receive the corresponding return value.

## CAPL Access

The control can be activated with the following CAPL functions:

- With the function setControlVisibility, you can set, if the control is displayed during runtime or not.

## Configuration

Assign a symbol to the control in the Panel Designer.

A function/method is always sent from the consumer to the provider. This means that the consumer sends the function and the provider responds. Accordingly, you can only connect the functions/methods of a client to the control. To do this, drag the desired endpoint to the Method Call Control.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

To enable you to adjust the size of the control optimally, the parameters are displayed immediately after linking to a function/method. The return values are only displayed at runtime of the panel.It is possible that the parameters may take up more space at runtime than the Panel Designer displays. Therefore, always check the size at runtime.

You can configure the control via the Properties Window.

## Display and Control Element

## Request

At runtime of CANoe/CANalyzer, you can set and send the parameters of the linked function on the Request page.

Click on the corresponding line and enter a value for the parameter. The [Send] button calls the function/method.

If the parameter is an array, you can open an editor for modifying the parameters with [...].The first column shows you the size of the array and the second column shows all elements of the array.

If a function/method contains optional parameters, the Send column is displayed in addition to the Parameter Name and Value column. By activating/deactivating the check box you determine whether the parameter is sent or not.If the parameters of the function/method are mandatory, the Send column remains empty.

The last column shows you whether the value was sent or whether t

[...truncated for brevity...]

### 控件: NMControl


# NM Control

Panel Designer » Windows » Toolbox » NM Control

## Use Cases

The NM Control can be used as a control and display element. With the NM Control you can control the OSEK NM DLL (oseknm01.dll) or the AutoSAR NM DLLs (AsrNM30.dll, AsrNM33.dll) on a simulated CAN bus in CANoe.

## Configuration

You can not assign a symbol to the NM Control. The corresponding system variables are assigned to the NM Control automatically.

Controlling during Run-Time

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. With the function enableControl, you can activate and deactivate the NM Control. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Font Group | Font |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you reduce the font size. |
|  | Font|Bold | With a click on the symbol you format the text bold. |
|  | Font|Italic | With a click on the symbol you format the text italic. |
|  | Font|Underline | With a click on the symbol you underline the text. |
| — | Font|Strikeout | Here you strikeout the text. |
| — | Font|Unit | Here you change the unit of the font size. |
|  | Text Color | Here you change the color of the text. CAPL Access With the function setControlForeColor, you can change the Text Color of the NM Controls. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |
|  | Background Color | Here you change the background color of the text. CAPL Access With the function setControlBackColor, you can change the Background Color of the NM Controls. With the function setControlColors, you can set the text and background colors in one step W

[...truncated for brevity...]

### 控件: NMControlRuntime


# NM Control: Controlling during Run-Time

Panel Designer » Windows » Toolbox » NM Control » Controlling during Run-Time

With the NM Control you can control the OSEK NM DLL (oseknm01.dll) or the AutoSAR NM DLLs (AsrNM30.dll, AsrNM33.dll) on a simulated CAN bus in CANoe.

The NM control lists all nodes that have a corresponding DLL assigned for the node in the Simulation Setup.

## Columns

| Column | Description | NM | AUTOSAR without PN* | AUTOSAR with PN* |
| --- | --- | --- | --- | --- |
|  | In the first column you specify whether the bus will be requested by the NM (Bus Request) or not (Bus Release). | ● | ● | ● |
| Node | Name of the respective node from the Simulation Setup. | ● | ● | ● |
| ID | Node address relevant for the NM. | — | ● | ● |
| RM | With this button you activate the Repeat Message Mode (only possible with own Bus Request). | — | ● | ● |
| IL | A green LED indicates that the Interaction Layer was activated. A gray LED indicates that the Interaction Layer was not activated. | ● | ● | ● |
| Act | This LED can be used as an operator control element. Here you can activate/deactivate the Application Activity in the NM with a click. This normally prevents the bus from being released even if an internal request is not present (see first column). A yellow LED indicates that the Application Activity was activated in the NM. | ● | ● | ● |
| NM | This LED can be used as an operator control element. Here you can stop the simulation of the NM DLL (CtrlSimulationOff) or start it (CtrlSimulationOn) with a click. A red LED indicates that the simulation of the NM DLL was stopped. | ● | ● | ● |
| State | State of the respective state machine of the NM DLL. | ● | ● | ● |

* PN: Partial Networks

## Buttons

The buttons at the bottom edge of the panel initiate actions on all nodes.

[NM Request All]

[NM Release All]

[IL Request All]

[IL Release All]

## AutoSAR NM with PN

For the AutoSAR NM with Partial Networks (AsrNM33.dll), the panel has a splitter on the right side.

With the splitter you open/close a Detail view with display and control elements for the node that you have selected on the left side under Nodes.

## Detail view

The Detail view displays all Partial Networks of the node with name and network ID.

On the far right it is indicated whether the node

- is an Activator for this network, i.e., the corresponding bit in its Send message will be set for Request

- will be awakened by this network (Remoted), i.e., the bit is part of its f

[...truncated for brevity...]

### 控件: NumericUpDown


# Numeric Up/Down

Panel Designer » Windows » Toolbox » Numeric Up/Down

## Use Case

Numeric Numeric Up/Down can be used as a control and display element for values within a defined value range.

The following use cases are possible with the Numeric Up/Down:

- Sets the port number

- Sets the data bytes used

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

Minimum and Maximum must be set in the Properties.

If Minimum/Maximum of the symbol are set in the database, these are applied automatically as the value range for the display scale. Otherwise, default values are assigned for the value range.

## Control Element

During runtime of CANoe/CANalyzer, you can select a value in Numeric Up/Down that is assigned to the symbol.

## Display Element

The symbol value is not set manually. Rather it is set by simulation or CAPL programs, for example. In the Numeric Up/Down this value is displayed.

|  | Note If the value of the assigned symbol exceeds the value range specified with Minimum and Maximum, the Numeric Up/Down remains in the uppermost or bottommost position. |

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Font Group | Font |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you reduce the font size. |
|  | Font|Bold | With a click on the symbol you format the text bold. |
|  | 

[...truncated for brevity...]

### 控件: PanelControlButton


# Panel Control Button

Panel Designer » Windows » Toolbox » Panel Control Button

## Use Case

With the Panel Control Button you can open Panels during the measurement.

|  | Note: Why is there also a Panel Control Button? CANoe/CANalyzer distinguishes between the following panels: Panels that are assigned to the CANoe/CANalyzer configuration (Home ribbon tab|Panel Configuration) Panels that are not assigned to the CANoe/CANalyzer configuration and are configured using the Panel Control Button. These are identified as referenced panels and appear in the list of referenced panels in the above-mentioned dialog. If a panel is configured in the CANoe/CANalyzer configuration as well as in the Panel Control Button, it is treated as a panel of the CANoe/CANalyzer configuration. |

You can use the Panel Control Button to open several referenced panels of an application range at the touch of a button and, at the same time, to automatically close referenced panels that are no longer needed.

The following use cases are possible with the Panel Control Button:

- You want to view all messages sent by the same network node.The signals of a send message are stored for each panel.Insert a Panel Control Button that opens all panels whose messages are sent from the same network node.Configure the Panel Control Button in such a way that all other panels are automatically closed.

- You receive a rest bus simulation for testing a control unit. You are only interested in a particular subset of the panels.Remove all panels from the configuration and create a panel in the CANoe/CANalyzer configuration. Insert a Panel Control Button on this panel in order to open and close those panels that are needed to test the control unit.

## Configuration

Create a panel in the Panel Designer to which you add the Panel Control Button. Select the referenced panels. Save the panel and add it to the CANoe/CANalyzer configuration.

During runtime of CANoe/CANalyzer, you can open the selected panels and close panels that are no longer needed at the touch of a button. Panels that are assigned to the CANoe/CANalyzer configuration are not considered, i.e., they will not be closed.

You can configure the control via the ribbon or the Properties Window.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name |

[...truncated for brevity...]

### 控件: PanelFileButton


# File Button

Panel Designer » Windows » Toolbox » File Button

## Use Case

With the File Button you can call up any desired file.

The following use cases are possible with the File Button:

- Starts a script. Once parameter and signal value definitions have been specified in an Excel file, the File Button is used to start a script that generates test cases with information from the Excel file.

- Opens a text file that displays information on the CANoe/CANalyzer configuration.

## Configuration

Assign a file to the File Button in the Panel Designer.

You can configure the control via the ribbon or the Properties Window.

During runtime of CANoe/CANalyzer you can open the selected file with the File Button.

If required, the program (Application) and also parameters can be provided along with the file, in order to open the file with the desired program.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Settings Group | Settings |  |
| Filename | Filename | Here you select the file that should be opened. |
| Application | Application | Here you select t the application to open the selected file. Note If a tool/program is already assigned for a particular file extension on your computer in Windows Explorer, it does not have to be reassigned in the Panel Designer. The file uses the information in Windows Explorer during runtime. |  | Note If a tool/program is already assigned for a particular file extension on your computer in Windows Explorer, it does not have to be reassigned in the Panel Designer. The file uses the information in Windows Explorer during runtime. |
|  | Note If a tool/program is already assigned for a particular file extension on your computer in Windows Explorer, it does not have to be reassigned in the Panel Designer. The file uses the information in Windows Explorer durin

[...truncated for brevity...]

### 控件: PathDialog


# Path Dialog

Panel Designer » Windows » Toolbox » Path Dialog

## Use Case

The Path Dialog is a control and display element for selecting files and folders interactively.

The following use cases are possible with the Path Dialog:

- Information about the path and the name of an Excel file that contains parameter and signal definitions. This file is used for the generation of test cases.

- Information about the logging file. The name and the path of the logging file are used in the Logging block of the CANoe/CANaylzer configuration.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

## Control Element

If you select a folder or file via in the File Dialog during the runtime of CANoe/CANalyzer, the information about the path and the name of the folder/file are stored in the symbol.

An existing path is opened with automatically.

## Display Element

The symbol value is not set manually. Rather it is set to a definite order/file by simulation or CAPL programs, for example. In the Path Dialog the corresponding content of the symbol is displayed.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Font Group | Appearance |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you reduce the font size. |
|  | Font|Bold | With a click on the symbol you format the text bold. |
|  | Font|Italic | W

[...truncated for brevity...]

### 控件: PictureBox


# Picture Box

Panel Designer » Windows » Toolbox » Picture Box

## Use Case

The Picture Box is a static element and is used for graphic display.

The following use cases are possible with the Picture Box:

- The Meter is stored with an image of an instrument panel. In this combination, it displays an instrument panel containing a tachometer and a speedometer with moving pointers.

- The windshield wipers to be tested are stored with an image of a windshield in order to provide a realistic appearance.

## Configuration

Assign an image to the Picture Box in the Panel Designer.

You can configure the control via the ribbon or the Properties Window.

During runtime of CANoe/CANalyzer the image is displayed on the panel.

|  | Note A Picture Box is always represented with a dashed-lane frame in the Panel Designer. This default setting allows you to recognize the Picture Box on the panel even without an assigned frame or image. The dashed-line frame is not shown in CANoe/CANalyzer. |

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| Appearance Group | Appearance |  |
| Image File | Image File | Here you change the image for the control. CAPL Access With the function setPictureBoxImage, you can exchange the image file during runtime. On the next measurement start, the image file selected in the Panel Designer will be reloaded. |
| Transparency | Transparent Color | Change the transparent color. The picture transparency is always active. You must only define the color for which the picture should be transparent. |
|  | Resize Proportionally | Resize Proportionally With a click on the symbol you activate/deactivate the proportional increase/decrease (height = width). |
|  | — | Fit Image Size With a click on the symbol you reset the selected image to its original size. |
|  | Border Style | Here you change the frame of the control: Fixed 3D3D frame Fixed SingleSingle frame NoneNo frame |
| More Group | — |  |
|  | — | Show Proper

[...truncated for brevity...]

### 控件: Pointer


# Pointer

Panel Designer » Windows » Toolbox » Pointer

The role of the pointer is to act as a marker tool within the Toolbox and nothing else.

Once a control has been assigned, the marker in the toolbox will automatically turn into a pointer. You can then configure the controls on the panel exactly as you wish.

Assigning Controls

| Version 12.0© Vector Informatik GmbH |  |


### 控件: ProgressBar


# Progress Bar

Panel Designer » Windows » Toolbox » Progress Bar

## Use Case

The Progress Bar is used to display a value within a defined value range in the form of a bar. The bar display allows you to quickly see whether the current value is in the lower, medium, or upper range of possible values.

The following use cases are possible with the Progress Bar:

- Display of engine speed.

- Display of vehicle acceleration.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

Minimum and Maximum must be set in the Properties.

If Minimum/Maximum of the symbol are set in the database, these are applied automatically as the value range for the display scale. Otherwise, default values are assigned for the value range.

## Display Element

During runtime of CANoe/CANalyzer the Progress Bar indicates the current symbol value.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| Font Group | Font |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you reduce the font size. |
|  | Font|Bold | With a click on the symbol you format the text bold. |
|  | Font|Italic | With a click on the symbol you format the text italic. |
|  | Font|Underline | With a click on the symbol you underline the text. |
| — | Font|Strikeout | Here you strikeout the text. |
| — | Font|Unit | Here you change the unit of the font size. |
|  | Text Color | Here you change the color of the text. |
|  | Background Color | Here you change the background color of

[...truncated for brevity...]

### 控件: RadioButton


# Radio Button

Panel Designer » Windows » Toolbox » Radio Button

## Use Case

The Radio Button can be used as a control and display element for triggering or displaying one option from a list of related options.

The following use cases are possible with the Radio Button:

- Display of signal status: The four ignition statuses are represented by four options. These are grouped in a Group Box.

- Control of open/closed door status for all doors.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

## Control Element

If you select the option during runtime of CANoe/CANalyzer, the switching value that you set in the Switch Value/Check property will be assigned to the symbol of the switching value.

## Display Element

The symbol is not set manually. Rather, it is set to a particular value, e.g., by simulation or CAPL programs, that is configured as a switching value in the Panel Designer. The option automatically appears as selected.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| Text | Text | Here you change the description of the control. |
|  | Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Font Group | Font |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you r

[...truncated for brevity...]

### 控件: StartStop


# Start Stop Control

Panel Designer » Windows » Toolbox » Start Stop Control

## Use Case

With the Start Stop Control, you can start and stop a measurement in both online and offline modes.

## Configuration

You can configure the control via the ribbon or the Properties Window.

If you start or stop the measurement from the CANoe/CANalyzer toolbar, the control indicates the current status.

If you start the measurement via CANoe/CANaylzer step-wise () or if you interrupt the measurement (), you can only stop the measurement using the control. If you want to restart the measurement after the step-wise measurement start or after the measurement interruption, you can only do this via the toolbar.

## Keyboard Operations

The function that is focused (Start or Stop) can be initiated with the space bar.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Border Style Group | Appearance |  |
|  | Border Style | Here you change the frame of the control: Fixed 3D3D frame Fixed SingleSingle frame NoneNo frame |
| More Group | — |  |
|  | — | Show Properties With a click on the symbol you open the Properties Window. |
| Group: — | Layout |  |
| — | Location/Size | Here you can enter settings relating to the size and position of the control. Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |  | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Snaplines appear on the working area to help you to line up the controls on the panel. |
|  | Note You can also resize the control by dragging its markers. Once selected, a control can be positioned anywhere on the panel. Sna

[...truncated for brevity...]

### 控件: StaticText


# Static Text

Panel Designer » Windows » Toolbox » Static Text

## Use Case

The Static Text is a static element for labeling items on the panel and nothing else.

The following use cases are possible with the Static Text:

- The purpose of a panel is described in an additional text.

- Describes instructions for the user.

## Configuration

The Static Text is created with the corresponding description in the Panel Designer.

You can configure the control via the ribbon or the Properties Window.

During runtime of CANoe/CANalyzer the description is displayed on the panel.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
| Text | Text | Here you change the description of the control. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| Font Group | Font |  |
| Font | Font|Name/Size | Here you change the font and the font size. |
|  | — | With a click on the symbol you increase the font size. |
|  | — | With a click on the symbol you reduce the font size. |
|  | Font|Bold | With a click on the symbol you format the text bold. |
|  | Font|Italic | With a click on the symbol you format the text italic. |
|  | Font|Underline | With a click on the symbol you underline the text. |
| — | Font|Strikeout | Here you strikeout the text. |
| — | Font|Unit | Here you change the unit of the font size. |
|  | Text Color | Here you change the color of the text. CAPL Access With the function setControlForeColor, you can change the Text Color of the Static Text. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultControlColors, you can reset the text and background colors to the default values defined in the Panel Designer. |
|  | Background Color | Here you change the background color of the text. CAPL Access With the function setControlBackColor, you can change the Background Color of the Static Text. With the function setControlColors, you can set the text and background colors in one step With the function setDefaultCont

[...truncated for brevity...]

### 控件: Switch


# Switch/Indicator

Panel Designer » Windows » Toolbox » Switch/Indicator

## Use Case

The Switch/Indicator can be used as a control and display element for selecting and displaying defined states.

Individual statuses are shown graphically.

The following use cases are possible with the Switch/Indicator:

- Depicts the conventional ignition lock, i.e., turning the ignition lock.

- Description of traffic light statuses red, yellow, green.

- Display of a digital fuel indicator.

## Special Features

The values entered during a state change can be concrete values and value ranges.

- Concrete values

- Value ranges

- When receiving (display element) the symbol, the system checks in which value range the symbol value lies and the corresponding state is displayed.

- For sending (control element), still a concrete value is required. If required, you can configure it in the Tx column.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

## Control Element

During runtime of CANoe/CANalyzer, you can actuate the Switch/Indicator; the corresponding switching value is assigned to the symbol and the Switch/Indicator displays the associated image.

## Display Element

The symbol is not set manually to a defined condition. Rather it is set by simulation or CAPL programs, for example. In the Switch/Indicator the associated image is displayed.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
|  | Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or n

[...truncated for brevity...]

### 控件: TabControl


# Tab Control

Panel Designer » Windows » Toolbox » Tab Control

## Use Case

The Tab Control is used to place controls on several tabs and enables the user to quickly switch between these tabs during runtime. No other panels have to be opened.

The following use cases are possible with Tab Control:

- Inserting a large variety of display and control possibilities, sorted by use cases.

- Executing individual actions on the various tabs and automatically opening the next tab.

- Configuring different variants of an ECU on various tabs and selecting the appropriate tab during the test.

## Configuration

When a new Tab Control is inserted, two tabs are automatically displayed. Additional tabs can be added.

Drag the controls from the toolbox to the desired tab, and arrange them using the displayed snap lines.

Assign a symbol to the added controls.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

| Selected Tab Control | Selected single tab (Vector Tab Page 1) |

Depending on the selection, you can configure the Tab Control or a single tab in the Properties Window:

A certain control on the Tab Control can be selected with the mouse or the Tab key.

You can select the tabs during runtime of CANoe/CANalyzer:

- With the mouse and with the arrow keysIf you have assigned a symbol to the Tab Control, this action changes and sends the symbol value.

- Via the assigned symbolYou can assign a symbol in the Properties Window that controls the selection of the tab. The numeric symbol value must be set during runtime to 1 for the first tab, 2 for the second tab, and so forth.

All control and display possibilities are available from the start of the measurement. Thus, for example, the display of a signal value starts without the related tab having been selected. If a film is running on a tab in a linked Media Player, the film continues running even if the user has switched to another tab.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here y

[...truncated for brevity...]

### 控件: TrackBar


# Track Bar

Panel Designer » Windows » Toolbox » Track Bar

## Use Case

The Track Bar can be used as a control and display element for values within a defined value range.

The following use cases are possible with the Track Bar:

- Display and setting of engine speed.

- Display of vehicle acceleration.

## Configuration

Assign a symbol to the control in the Panel Designer.

You can assign a symbol to the control

- by dragging and dropping it from the Symbol Explorer

- by opening the corresponding Symbol Selection dialog:

- click the links at the bottom of the Properties Window

- under Symbol (once you have selected the symbol filter)

- via the context menu

You can configure the control via the ribbon or the Properties Window.

Minimum and Maximum must be set in the Properties.

If Minimum/Maximum of the symbol are set in the database, these are applied automatically as the value range for the display scale. Otherwise, default values are assigned for the value range.

|  | Note If the value of the assigned symbol exceeds the value range specified with Minimum and Maximum, the Track Bar remains in the rightmost or leftmost position. |

## Control Element

During runtime of CANoe/CANalyzer, the Track Bar can be used to set a desired value; this value is assigned to the symbol.

## Display Element

The symbol value is not set manually. Rather it is set by simulation or CAPL programs, for example. In the Track Bar this value is displayed.

## Ribbon|Properties Tab / Properties Window

Here all settings are listed that you can change in the ribbon and/or in the Properties Window.

| Ribbon | Properties Window | Description |
| --- | --- | --- |
| General Group | General |  |
| Name | Control Name | Here you change the name of the control. This name and the name of the panel is required for access from CAPL. |
|  | Display Only | Display Only With a click on the symbol you switch between control and display element. With activated option the control is used as display element. |
| — | Is Visible At Runtime | Specifies whether the control is to be displayed during runtime. CAPL Access With the function setControlVisibility, you can set, if the control is displayed during runtime or not. |
| — | Tab Index | Defines the order in which the various controls on a panel are to be navigated with the Tab key during runtime. |
| Value Range Group | Value Range |  |
| Minimum | Minimum | Here you change the minimum of the value range. |
| Maximum | Maximum | Her

[...truncated for brevity...]

### 控件: PanelDesignerNetNodes


## Network Nodes

System components with specific functionality are referred to as network nodes or controllers. This includes behavior relating to input and output variables as well as messages to be received and sent out. To describe network nodes functionally CANoe provides the event-driven procedural language CAPL. Using this tool the user could, for example, describe how the received data should be processed after a message arrives, and how it should output the result as a control value. Network nodes are represented in the Simulation Setup in CANoe.

| Version 12.0© Vector Informatik GmbH |  |


---

## Panel 操作步骤 (Procedures)

### PanelDesignerAssigneControls


# Assigning Controls

Panel Designer » Windows » Toolbox » Assigning Controls

You can assign the controls from the toolbox to the panel in various ways:

- Using drag and drop

- By double-clicking

- By clicking with the left mouse button to select the required control and then clicking again with the left mouse button on the panel

| Version 12.0© Vector Informatik GmbH |  |


### PanelDesignerGridLines


# Aligning Controls

Panel Designer » Windows » Working Area » Aligning Controls

### Snaplines

In the Options dialog you can enter the alignment settings for controls within a panel:

- Controls snap to snaplines

- Controls snap to grid

- Controls free positionable

## Keyboard Operations

| Functional description | Key combination |
| --- | --- |
| Move the control on the panel pixel-by-pixel | <>, <>, <>, <> |
| Move the control along the snaplines | <Ctrl>+<>, <>, <>, <> |
| Increase or decrease the height of the control pixel-by-pixel | <Shift>+<> or <Shift>+<> |
| Increase or decrease the width of the control pixel-by-pixel | <Shift>+<> or <Shift>+<> |
| Increase or decrease the height of the control to the next snapline | <Shift>+<Ctrl>+<> or <Shift>+<Ctrl>+<> |
| Increase or decrease the width of the control to the next snapline | <Shift>+<Control>+<> or <Shift>+<Control>+<> |
| Use the mouse to deactivate snaplines when moving the control | <Alt>+mouse movement |
| Copy controls | Select the controls, press <Ctrl> and use the mouse to drag to the required position (the insert symbol appears at the cursor ), release the mouse button, release <Ctrl>. |
| Proportionally change the size. Available for: New Panel LED Control Picture Box Switch/Indicator | Select the controls, press <Shift> and change the size using the mouse on the mark frame. This function is not available for dragging on corners. |

| Version 12.0© Vector Informatik GmbH |  |


### PanelDesignerMultiselect


# Selecting Several Controls (Multiple Selection)

Panel Designer » Windows » Working Area » Selecting Several Controls (Multiple Selection)

It is possible to select several controls at the same time, for example if you want to modify shared properties in one step.

You can make multiple selections in a variety of ways:

- 'Capturing' controls with the mouse

Hold down the left mouse button and drag the mouse to create a rectangular selection frame that encompasses the controls you want to select. Release the left mouse button.The selected controls are highlighted, and small white or black squares appear on the outer edges of the controls.

- Selecting controls using the keyboard

- Select a control in the panel. The first selected control is highlighted, and small white squares appear on its outer edges.

- To select additional controls, hold down the <Shift> key and select further controls. These are now also highlighted, and small black squares appear on the outer edges of the controls.

|  | Note In this case it may happen that all the controls and the panel itself are selected. This may give you the impression that you cannot deselect the multiple selection.The solution here is to deselect the panel by pressing the <Shift> key again and clicking on the edge of the panel or directly in a free area of the panel. |

|  | Note The first control that you select will have small white squares on its outer edges. It is the leading control and as such, its properties are used for modifications e.g. for Layout functions like setting the same width. |

| Version 12.0© Vector Informatik GmbH |  |


### PanelDesignerOpenPanelEditor


# Opening the Panel Designer

Panel Designer » Opening the Panel Designer

To open the Panel Designer do one of the following:

- Via the CANoe/CANalyzer Tools ribbon tab:

- Choose the Edit command from the context menu of an opened panel. This panel is then loaded and displayed in the Panel Designer.

| Version 12.0© Vector Informatik GmbH |  |


### PanelDesignerSymbolDisplay


# Displaying assigned Symbols

Panel Designer » Displaying assigned Symbols

## Panel Designer

Assignments between symbols and controls are displayed in the status bar of the Panel Designer.

## CANoe/CANalyzer

Assignments between symbols and controls can be displayed in CANoe/CANalyzer by positioning the cursor on any control.

The assigned symbol is displayed in a ScreenTip to the lower right of the tip of the cursor.

| Version 12.0© Vector Informatik GmbH |  |


### PanelDesignerValueTables


# Working with Value Tables

Panel Designer » Working with Value Tables

For the controls Button, Check Box, LED Control, Media Player, Radio Button and Switch/Indicator, you can assign switch values from value tables.

## Advantage over Numerical Switch Values

In the value tables a symbolic value is assigned to a numerical value, e.g. 3 = Warning

If you have configured a symbolic value as switch value (e.g. Warning), the behavior of the controls does not change when the numerical value changes.

Controls with numerical switch values must be adapted as soon as a numerical specification changes.

## What Happens when Working with a Numerical Value or a Value from a Value Table

The following example is intended to explain the behavior between two Radio Buttons.

## Configuration in Panel Designer

- System variables with value table assigned to both Radio Buttons.

- Radio Button 1 is configured with the numerical switch value 3.

- Radio Button 2 is configured with the symbolic switch value Warning from the value table.

## Behavior at Run-time

| Behavior | Radio Button 1 Configured Switch Value: 3 | Radio Button 2 Configured Switch Value: Warning |
| --- | --- | --- |
| Case 1: The value table of the system variable is changed before the measurement: The numerical value changes to 4, the symbolic value remains Warning |
| Receiving | The Radio Button is not activated (4!=3) | The Radio Button is activated (Warning=Warning) |
| Sending | By pressing the Radio Button, the value 3 is still sent; it may no longer trigger the desired action. | By pressing the Radio Button, Warning is still sent. |
| Case 2: The value table of the system variable is changed before the measurement: The numerical value remains 3, the symbolic value changes to Error |
| Receiving | The Radio Button is activated (3=3) | The Radio Button is not activated (Error!=Warning) |
| Sending | By pressing the Radio Button, the value 3 is still sent; it may no longer trigger the desired action. | B

[...truncated for brevity...]

---

## Panel 通用说明 (General)

### CopyrightContact


# Contact/Copyright/License

Panel Designer » Contact/Copyright/License

## Contact

Vector Informatik GmbH

Ingersheimer Str. 2470499 StuttgartGermany

http://www.vector.com

## Imprint

Vector reserves the right to modify any information and/or data in this user documentation without notice. This documentation nor any of its parts may be reproduced in any form or by any means without the prior written consent of Vector. To the maximum extent permitted under law, all technical data, texts, graphics, images and their design are protected by copyright law, various international treaties and other applicable law. Any unauthorized use may violate copyright and other applicable laws or regulations.

© Copyright Vector Informatik GmbH

All rights reserved.

## Protected Trademarks

All brand names in this documentation are either registered or non registered trademarks of their respective owners.

## Additional Copyrights/License Notes

According to the license, you may get the original sources as well as the partly changes from support@vector.com.

| Copyright/License for… | Note |
| --- | --- |
| Ace | Copyright (c) 2010, Ajax.org B.V. See complete text for further details: License to BSD Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. Neither the name of Ajax.org B.V. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 

[...truncated for brevity...]

### PanelDesignerCaplFunctions


# Access Panels using CAPL Functions

Panel Designer » Access Panels using CAPL Functions

You can access panels or panel elements using following CAPL functions.

| CAPL Function | Description | Panel Designer Controls |
| --- | --- | --- |
| openPanel | Opens a panel or all panels. | — |
| closePanel | Closes a panel or all panels. | — |
| clockControlReset | Resets the Clock Control designed as stop watch. | Clock Control |
| clockControlStart | Starts the Clock Control designed as stop watch. | Clock Control |
| clockControlStop | Stops the Clock Control designed as stop watch. | Clock Control |
| deleteControlContent | Deletes the contents of the CAPL Output View. | CAPL Output View |
| enableControl | Activates or deactivates specific elements. | Button; Check Box; Combo Box; Hex/Text Editor; Input/Output Box; MOST Send Button; Numeric Up/Down; Panel Control Button; Path Dialog; Radio Button; Switch/Indicator; Track Bar |
| putValue | Transfers defined values to the symbol assigned to the control. | Analog Gauge, Button, Check Box, Clock Control, Combo Box, Hex/Text Editor, Input/Output Box, LCD Control, Media Player, Meter, Numeric Up/Down, Path Dialog, Progress Bar, Radio Button, Switch/Indicator, Track Bar |
| putValueToControl | Transfers defined values to the control. Note Since CANoe/CANalyzer version 7.5 for the putValueToControl function additional parameters can be set to change the format of the output, e.g. the text should be displayed in a new paragraph or the value should be displayed hexadecimal. |  | Note Since CANoe/CANalyzer version 7.5 for the putValueToControl function additional parameters can be set to change the format of the output, e.g. the text should be displayed in a new paragraph or the value should be displayed hexadecimal. | CAPL Output View |
|  | Note Since CANoe/CANalyzer version 7.5 for the putValueToControl function additional parameters can be set to change the format of the output, e.g. the text should be displayed in a ne

[...truncated for brevity...]

### PanelDesignerComparisonDesignerEditor


# Panel Desiger / Panel Editor

Panel Designer » Panel Desiger / Panel Editor

This sides shows you an overview about the functionality and controls of Panel Designer and Panel Editor.

| Functionality | Panel Designer | Panel Editor |
| --- | --- | --- |
| Create control and display elements | • | • |
| Import Panel Editor panels (*.cnp) & Remote Control panels (*.oci; MOST specific) | • | — |
| Create panels using drag and drop | • | — |
| Configure controls using drag and drop | • | — |
| Automatically generate panels | — | • |
| Automatically assign to configuration | • | — |
| Test mode for checking the functionality of the controls | — | • |
| Operate the controls using CAPL functions (activate/deactivate panel, define colors) | • | • |
| Panel file format | *.xvp | *.cnp |
| Window management |  |  |
| Docked windows (Toolbox, Properties, Symbol Explorer) | • | — |
| Panel layout, align controls |  |  |
| Align functions | • | • |
| Snaplines | • | — |
| Key Combinations | • | — |
| Undo/Redo function | • | • |
| Controls |  |  |
| Analog Gauge | Analog Gauge |
| Button | Push Button Bitmap Push Button |
| CAPL Output View | Multi Display Control |
| Check Box | — |
| Clinometer | — |
| Clock Control | Clock Control |
| Combo Box | Value Table Box |
| Compass | — |
| Group Box | Frame |
| Hex/Text Editor | Hex Editor |
| Input/Output Box | Input/Output Box; Alarm_States_Indicator |
| LCD Control | LCD Display |
| LED Band | — |
| LED Control | — |
| Numeric Up/Down | Spin Control |
| Media Player | — |
| Media Stream Control | — |
| Meter | Meter |
| Method Call Control | — |
| MOST Send Button | MOST BMP Button |
| Panel Control Button | Panel Control Button |
| File Button | Panel Help Button |
| Path Dialog | FileSelection |
| Picture Box | Bitmap; Static_Bitmap |
| Progress Bar | VectorBar |
| Radio Button | Radio Button |
| Start Stop Control | — |
| Static Text | Text |
| Switch/Indicator | Switch, Bitmap Switch/Indicator, Bitmap_Button, Bitmap_Switch 

[...truncated for brevity...]

### PanelDesignerCompatibility


# Compatibility

Panel Designer » Compatibility

## Loading panel files in CANoe/CANalyzer

- Created panel files can be loaded and displayed in CANoe and CANalyzer.

|  | Note CANalyzer pro/CANalyzer exp supports: Display elements with assigned signals and system variables Control elements with assigned system variables CANalyzer fun supports only display elements with assigned signals System variables are not supported by CANalyzer fun. In CANalyzer all control and display elements with assigned environment variables will automatically be deactivated, due to the fact that environment variables are not supported in CANalyzer. |

## Loading panel files from newer versions

- Created panel files from newer CANoe/CANalyzer versions can be loaded and displayed in this version.

|  | Note Only functions of this version are supported. Functions of the newer version will automatically be deactivated. If you save a loaded panel file with this version, all functions of the new version will get lost. |

- Created panel files since CANoe/CANalyzer version 7.0 SP4 can not be loaded and displayed in older versions.

Solution:

Install the current Service Pack for version 7.0. You can find this on www.vector.com

## Loading panel files in Panel Designer and Panel Editor

- In the Panel Designer created panel files (*.xvp) can only be opened and edited in the Panel Designer.

- In the Panel Editor created panel files (*.cnp) can only be opened and edited in the Panel Editor.

## Convert panels into Panel Designer panels

Panel Editor panels (*.cnp) and Remote Control panels (*.oci) can be converted into Panel Designer panels using the Import function.

Restricted Mode | Panel Desiger / Panel Editor

| Version 12.0© Vector Informatik GmbH |  |


### PanelDesignerConversionRules


# Panel Conversion: Notes

Panel Designer » Panel Conversion » Notes

You can use the Panel Designer's Import function to convert Panel Editor panels (CNP files) into Panel Designer panels (XVP files).

The most important conversion rules are listed below.

## Converting a Panel Editor Multi Display Control into a Panel Designer CAPL Output View

The Multi Display Control of the Panel Editor is converted into the CAPL Output View element of the Panel Designer.

The Multi Display Control can only display one output, which is overwritten by the next output. When the CAPL Output View element is generated, it exhibits the same behavior, i.e. the Output Mode property is set to Overwrite.

## Converting a Panel Editor Clock Control into a Panel Designer Clock Control

The Clock Control of the Panel Editor is converted into the Clock Control of the Panel Designer.

The following use cases for the Panel Editor control are converted:

- Display of the PC's system time (PC time)

- The Panel Editor control properties are set to Clock Mode = Clock and Input Source = SystemTime.

- The converter generates a new Clock Control.

- The clock is functional immediately after the conversion has taken place.

- Transmission of the time from CAPL to the Clock Control at runtime.

- The Panel Editor control properties are set to Clock Mode = Clock and Input Source = CAPL.

- The converter generates a new Clock Control.

- The clock is not functional after the conversion has taken place.

- You need to adapt the CAPL time-setting function to this new function; see Clock Control.

- Use as a stopwatch, synchronized to the PC time.

- The Panel Editor control properties are set to Clock Mode = StopWatch and Input Source = SystemTime.

- The converter generates a new Clock Control.

- The stopwatch is not functional after the conversion has taken place.

- You need to adapt the CAPL functions that set the stopwatch to this new function; see Clock Control.

The following Panel Editor use ca

[...truncated for brevity...]

### PanelDesignerCreatingBitmaps


# Assigning and Creating Bitmaps

Panel Designer » Assigning and Creating Bitmaps

You can create and edit bitmap files with any bitmap editor (e.g. Paint, Photoshop).

A bitmap file for a n-stage switch always consists of n+1 rectangular partial bitmaps, each with the same height and width, arranged to be horizontally adjacent to one another.

In the first rectangle the inactive state is shown. This appears on the panel when no symbol has been assigned to the element. The Switch/Indicator shows the inactive state as long as the assigned Signal will be received.

The n switch values are located in the n partial bitmaps to the right of this.

|  | Example of Two-Stage Switch |

|  | Note When creating your own bitmaps be sure to save them as uncompressed Windows bitmaps. Some graphics drivers cannot process specially compressed bitmaps, which may result in undesirable optical effects or even system crashes. It is advisable to save all bitmaps belonging to a panel in a separate subdirectory. If you wish to forward a panel to another user you must also forward the bitmap directory. |

| Version 12.0© Vector Informatik GmbH |  |


### PanelDesignerDisplayBinValues


# Displaying and Entering Binary Values

Panel Designer » Binary Display

Binary display is supported in the Input/Output Box and the Combo Box in the Panel Designer. The Input/Output Box also supports the entry of binary values.

Signals, environment variables and system variables can be displayed and entered in binary format if their raw or physical value is an integer.

The Combo Box can only display raw values.

## Displaying Raw Values in Binary Format

Depending on the symbol definition, integer values are displayed binary. Leading zeros are not displayed in this case.

|  | Example: Displaying Raw Values Signal definition Min/Max values Signal places (Bin) Values (Bin) 3 Bit, signed -43 3 10011 3 Bit, unsigned 07 3 0111 8 Bit, signed -128127 8 100000001111111 8 Bit, unsigned 0255 8 011111111 | Signal definition | Min/Max values | Signal places (Bin) | Values (Bin) | 3 Bit, signed | -43 | 3 | 10011 | 3 Bit, unsigned | 07 | 3 | 0111 | 8 Bit, signed | -128127 | 8 | 100000001111111 | 8 Bit, unsigned | 0255 | 8 | 011111111 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Signal definition | Min/Max values | Signal places (Bin) | Values (Bin) |
| 3 Bit, signed | -43 | 3 | 10011 |
| 3 Bit, unsigned | 07 | 3 | 0111 |
| 8 Bit, signed | -128127 | 8 | 100000001111111 |
| 8 Bit, unsigned | 0255 | 8 | 011111111 |

## Displaying Physical Values in Binary Format

- Depending on the symbol definition, integer values are displayed binary. Leading zeros are not displayed in this case.

- Signals with a Signed Integer or Unsigned Integer data type can be displayed binary.

- The physical value range of integer signals with Factor = 1 and Offset = 0 corresponds exactly to the value range of the underlying data type. In this case the physical value is identical to the raw value.

- However, if you define Factor and Offset values, this results in a physical value range that differs from the v

[...truncated for brevity...]

### PanelDesignerDisplayHexValues


# Displaying and Entering Hexadecimal Values

Panel Designer » Hexadecimal Display

Hexadecimal display is supported in the Input/Output Box and the Combo Box in the Panel Designer. The Input/Output Box also supports the entry of hexadecimal values.

Signals, environment variables and system variables can be displayed and entered in hexadecimal format if their raw or physical value is an integer.

The Combo Box can only display raw values.

## Displaying Raw Values in Hexadecimal Format

Depending on the symbol definition, integer values are filled to form full bytes and displayed hexadecimally. Leading zeros are not displayed in this case.

|  | Example: Displaying Raw Values Signal definition Min/max values Signal places (Hex) Value (Hex) 3 bit, signed -43 2 FC3 3 bit, unsigned 07 2 07 8 bit, signed -128127 2 807F 8 bit, unsigned 0255 2 0FF | Signal definition | Min/max values | Signal places (Hex) | Value (Hex) | 3 bit, signed | -43 | 2 | FC3 | 3 bit, unsigned | 07 | 2 | 07 | 8 bit, signed | -128127 | 2 | 807F | 8 bit, unsigned | 0255 | 2 | 0FF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Signal definition | Min/max values | Signal places (Hex) | Value (Hex) |
| 3 bit, signed | -43 | 2 | FC3 |
| 3 bit, unsigned | 07 | 2 | 07 |
| 8 bit, signed | -128127 | 2 | 807F |
| 8 bit, unsigned | 0255 | 2 | 0FF |

## Displaying Physical Values in Hexadecimal Format

- Depending on the symbol definition, integer values are filled to form full bytes and displayed hexadecimally. Leading zeros are not displayed in this case.

- Signals with a Signed Integer or Unsigned Integer data type can be displayed hexadecimally.

- The physical value range of integer signals with Factor = 1 and Offset = 0 corresponds exactly to the value range of the underlying data type. In this case the physical value is identical to the raw value.

- However, if you define Factor and Offset values, this results

[...truncated for brevity...]

### PanelDesignerFunctionOverview


# Function Overview

Panel Designer » Function Overview

| Creating and saving panels |
| --- |
| You can use the Panel Designer to create graphic panels on which the values of symbols can be modified and displayed interactively by the user during simulation. As the working area has been designed to work on the basis of tabs, multiple panels can be opened simultaneously in parallel. A symbol from the database must be assigned to each display and control. The panels are saved in xvp (extended vector panel) format and can subsequently be loaded in CANoe/CANalyzer configurations. |
| Assigning and aligning controls |
| All controls can be assigned to an open panel directly from the toolbox: Using drag and drop By double-clicking By clicking with the left mouse button to select the required control and then clicking again with the left mouse button on the panel To facilitate alignment of the controls, snaplines on which controls can be aligned appear when you start the assignment process. Supplementing the guide lines, the Home ribbon tab features additional edit options. The following control types are available for the configuration of the panels: Display elements Control elements Static elements |
| Panel and control configuration |
| Individual panels and controls are configured via the ribbon or the Properties Window. All significant settings for one or a number of selected elements can be made in this window. You can use the Input/Output Box or the Combo Box to display and enter values in hexadecimal or binary format. |
| Assigning symbols |
| The available symbols can be assigned directly to a control by dragging and dropping from the Symbol Explorer. If you drag and drop a Symbols to a panel directly, this symbol is assigned to the default control set in the Options dialog. Supported symbols depend on the CANoe/CANalyzer program variant. When a signal is assigned, the minimum/maximum values from the database are used for the value range (min/max) or for the ala

[...truncated for brevity...]

### PanelDesignerGlossary


# Glossary

Panel Designer » Glossary

## Symbols

|  | Definition Symbols In CANoe/CANalyzer symbols are system variables, environment variables, signals, diagnostics parameter and communication objects. With symbols values can be displayed or actions can be triggered. |

Linking of symbols to panel controls is done directly in the Panel Designer.

The following symbols are available in the Panel Designer:

- Environment variables

Environment variables represents the connection between a specific control on the panel and the associated CAPL program. In the CAPL program a change in the value of the environment variables causes a reaction, thereby triggering a specific action.

|  | Note Environment variables are only supported for panels used in CANoe. |

- Signals

Because of the association of signals, signal values can also be set with the controls. This requires the availability of an Interaction Layer.

If a signal value is changed by a control, the control is initially shown with red hatch marks. This red hatching indicates that the value shown by the control is not synchronous to the bus, i.e. the new value was not yet sent on the bus. As soon as a message has been transmitted on the bus with the relevant signal, the red hatching disappears, since the control is now in a bus-synchronous state.

|  | Note If you have assigned a SOME/IP Service Signal that contains at least one array, the desired index of the array can be specified in the Properties Window (property Array Index Qualifier, Symbol category). Select the input box with the mouse, and specify the desired index inside square brackets. In CANalyzer the changing of signal value is not possible. |

- System variables

CANoe/CANalyzer system variables are similar to environment variables, but instead of the database, they are defined in the respective context.

System variables are categorized and can store values of type character string (string), integers (int), or floating points (float). It is also

[...truncated for brevity...]

### PanelDesignerRefPanels


# Referenced Panels

Panel Designer » Properties Window » Panel Control Button » Referenced Panels

In the Referenced Panels dialog you can assign panels to the Panel Control Button.

|  | Note In CANalyzer Network Panels and Node Panels are not available. |

- Network Panels

With [Add] you open the Symbol Selection Dialog. Here you can select the Rx nodes of your Network Panel.The selected Network Panel is opened when the Panel Control Button is pressed during run-time. The selected Rx nodes are displayed automatically.

- Node Panels

With [Add] you open the Symbol Selection Dialog. Here you can select the Tx nodes of your Node Panel.The Node Panels for the selected Tx nodes are opened when the Panel Control Button is pressed during run-time.

- Referenced Panels

With [Add] you open the Windows Explorer. Here you can define which panels will be opened when clicking the Panel Control Button.No Panel Editor panels (CNP) can be referenced.

With [Remove] you can delete assigned panels from the list.

| Version 12.0© Vector Informatik GmbH |  |


### PanelDesignerRestrictedMode


# Restricted Mode

Panel Designer » Restricted Mode

In CANalyzer fun/CANoe run the Panel Designer is opened in a restricted mode.

This means that all available panels can be opened and edited - but only with the following restrictions:

- Only display elements and combined control and display elements are available and values can't be changed interactively.

- Elements that are configured as combined control and display elements can only be used as a display.

Controls | Compatibility | Supported Symbols in CANoe /CANalyzer program variants

| Version 12.0© Vector Informatik GmbH |  |


### PanelDesignerTransparency


# Transparency Color

Panel Designer » Transparency Color

Bitmap elements whose transparency is active allow the background to appear through their areas of transparency color. That is, the transparency color remains invisible. This allows these elements to represent any desired forms.

To draw a bitmap with transparency fill the areas that should be transparent with the color you have defined in the ribbon in the Transparency field or in the Properties Window in the Transparent Color field.The default setting of the transparency color is Blue (RGB 0,0,255).

|  | Note Use the default color Blue (RGB 0.0255) to create bitmaps with transparent color. Then have not to choose always a new transparent color for each newly added bitmap in the Panel Designer. |

Elements such as Button, Track Bar, Input/Output Box or Static Text do not appear through the transparency areas of Picture Box and Switch/Indicator if they are placed below them.When overlapping Picture Box and Switch/Indicator, the transparency remains active.

| Version 12.0© Vector Informatik GmbH |  |

