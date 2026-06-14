# VT System CAPL Functions

> Category: `VTSystem` | Type: `notes`

## Description

General Methods/Functions

Trigger Methods/Functions

VT1004/VT1104 related Methods/Functions

VT2004 related Methods/Functions

VT2516 Methods/Functions

VT2808 related Methods/Functions

VT2816 related Methods/Functions

VT2832 related Methods/Functions

VT2848 related Methods/Functions

VT7001 related Methods/Functions

VT8006A/VT8012A related Methods/Functions

Trigger Methods/Function [▲ back]

VT System | Enumeration

| VT SYSTEM The methods/functions listed on this site can only be called in connection with system variables. Information about the differences between methods and functions can be found here. |
|---|

| General Methods/Functions Trigger Methods/Functions VT1004/VT1104 related Methods/Functions VT2004 related Methods/Functions VT2516 Methods/Functions | VT2808 related Methods/Functions VT2816 related Methods/Functions VT2832 related Methods/Functions VT2848 related Methods/Functions VT7001 related Methods/Functions VT8006A/VT8012A related Methods/Functions |
|---|---|

| Methods/Functions | Short Description |
|---|---|
| SetTransferCycle vtsSetTransferCycle | Sets the cycle time for retrieving the corresponding value from the VT System. |

| Methods/Functions | Short Description |
|---|---|
| SetTriggerParams vtsSetTriggerParams | Configures basic parameters for triggers. |
| SetTriggerParamsEx vtsSetTriggerParamsEx | Configures additional parameters for VT System triggers. |
| StartTrigger vtsStartTrigger | Starts the specified trigger. It also resets the event counter system variable that is associated to the trigger to 0. |

| Methods/Functions | Short Description |
|---|---|
| ResetMinMax vtsResetMinMax | Resets the minimum and maximum value. |
| SetLoadMode vtsSetLoadMode | Sets the mode for internal load. |
| SetMeasurementMode vtsSetMeasurementMode | Sets the mode for voltage measurement. |
| SetLoadControlTimeout vtsSetLoadControlTimeout | Sets the timeout for the internal load. |
| SetPWMMeasurementDuration vtsSetPWMMeasurementDuration | Sets the PWM evaluation raster. |
| SetPWMThreshold vtsSetPWMThreshold | Sets the PWM trigger threshold. |
| SetImpedanceMode vtsSetImpedanceMode | Switches for VT1004A between the mode with high impedance (default state) and low impedance. |
| SetIntegrationTime vtsSetIntegrationTime | Sets the integration time for average and RMS values. |

| Methods/Functions | Short Description |
|---|---|
| LoadWFResistance vtsLoadWFResistance | Loads a resistance curve for a channel from a specified file. |
| LoadWFVoltage vtsLoadWFVoltage | Loads a voltage curve for a channel from a specified file. |
| SetCurveType vtsSetCurveType | Sets the mode of the curve. |
| SetStimulationMode vtsSetStimulationMode | Sets stimulation mode. |
| StartStimulation vtsStartStimulation | Starts stimulation output. |
| StopStimulation vtsStopStimulation | Stops stimulation output. |
| SetPWMResistanceLow vtsSetPWMResistanceLow | Sets the resistance value for low on PWM output. |
| SetPWMStartDelay vtsSetPWMStartDelay | Sets the delay of the start for the output of PWM signals and curves. |
| SetPWMResistanceHigh vtsSetPWMResistanceHigh | Sets the resistance value for high on PWM output. |
| SetPWMVoltageLow vtsSetPWMVoltageLow | Sets the low voltage on PWM output. |
| SetPWMVoltageHigh vtsSetPWMVoltageHigh | Sets the high voltage on PWM output. |
| SetPWMRepeats vtsSetPWMRepeats | Sets the number of stimulated PWM periods after the start of stimulation. |
| SetWFParams vtsSetWFParams | Configures the parameters for the output of a voltage or resistance curve. |

| Methods/Functions | Short Description |
|---|---|
| LoadWFBitStream vtsLoadWFBitStream | The function loads a bit stream for the channel from the specified file. |
| SetCurveType vtsSetCurveType | Sets the mode of the bit stream. |
| SetIntegrationTime vtsSetIntegrationTime | Sets the integration time for average values. |
| SetPWMMeasurementDuration vtsSetPWMMeasurementDuration | Sets the max evaluation time for PWM signals. |
| SetPWMRepeats vtsSetPWMRepeats | Sets the number of stimulated PWM periods after the start of stimulation. |
| SetPWMVoltageHigh vtsSetPWMVoltageHigh | Sets the high voltage on digital output. |
| SetPWMVoltageLow vtsSetPWMVoltageLow | Sets the low voltage on digital output. |
| SetStimulationMode vtsSetStimulationMode | Sets stimulation mode. |
| SetThreshold1_8 vtsSetThreshold1_8 | Sets the threshold value for differentiating between high and low levels of the channels 1…8 of a digital module VT2516. |
| SetThreshold9_16 vtsSetThreshold9_16 | Sets the threshold value for differentiating between high and low levels of the channels 9…16 of a digital module VT2516. |
| SetWFParams vtsSetWFParams | Configures the parameters for the output of a bit stream. |
| StartStimulation vtsStartStimulation | Starts stimulation output. |
| StopStimulation vtsStopStimulation | Stops stimulation output. |

| ResetMinMax vtsResetMinMax | Resets the minimum and maximum value. |
|---|---|
| SetMinCurrentMeasurementRange vtsSetMinCurrentMeasurementRange | Sets the current measurement range that should be used from the automatic measuring range changeover of the VT2808 module. |

| Methods/Functions | Short Description |
|---|---|
| LoadWFVoltage vtsLoadWFVoltage | Loads a voltage curve for a channel from a specified file. |
| ResetMinMax vtsResetMinMax | Resets the minimum and maximum value. |
| SetCurveType vtsSetCurveType | Sets the mode of the bit stream. |
| SetIntegrationTime vtsSetIntegrationTime | Sets the integration time for average and RMS values. |
| SetMeasurementMode vtsSetMeasurementMode | Sets the mode for voltage measurement. |
| SetOutputRange vtsSetOutputRange | Sets the range that is used for analog output on output channels of VT2816 modules. |
| SetWFParams vtsSetWFParams | Configures the parameters for the output of a bit stream. |
| StartStimulation vtsStartStimulation | Starts stimulation output. |
| StopStimulation vtsStopStimulation | Stops stimulation output. |

| Methods/Functions | Short Description |
|---|---|
| SetOutputMask | Activates the requested rows of a switch matrix module for dynamic stimulation. |
| vtsSetOutputMask | Activates the requested rows of a switch matrix module for dynamic stimulation. |

| Methods/Functions | Short Description |
|---|---|
| LoadWFBitStream vtsLoadWFBitStream | The function loads a bit stream for the channel from the specified file. |
| SetCurveType vtsSetCurveType | Sets the mode of the bit stream. |
| SetOutputMode vtsSetOutputMode | Sets the mode for output on the channel. |
| SetOutputSource vtsSetOutputSource | Sets the source for the high voltage level for output. |
| SetPWMMeasurementDuration vtsSetPWMMeasurementDuration | Sets the max evaluation time for PWM signals. |
| SetPWMRepeats vtsSetPWMRepeats | Sets the number of stimulated PWM periods after the start of stimulation. |
| SetPWMStartDelay vtsSetPWMStartDelay | Sets the delay of the start for the output of PWM signals and curves. |
| SetThreshold vtsSetThreshold | Sets the threshold value for differentiating between high and low levels of a group of channels on a VT2848 module. |
| SetWFParams vtsSetWFParams | Configures the parameters for the output of a bit stream. |
| StartStimulation vtsStartStimulation | Starts stimulation output. |
| StopStimulation vtsStopStimulation | Stops stimulation output. |

| Methods/Functions | Short Description |
|---|---|
| <OnSerialError> | Is called when an error has occurred in an operation on a serial port. |
| <OnSerialReceive> | Is called when data has been received from the assigned serial port. |
| <OnSerialSend> | Is called when a send operation has been completed on the assigned serial port. |
| LoadWFVoltage vtsLoadWFVoltage | Loads a control voltage curve for a power supply from a specified file. |
| ResetMinMax vtsResetMinMax | Resets the minimum and maximum value. |
| SerialClose vtsSerialClose | Closes the serial port of the VT System channel. |
| SerialConfigure vtsSerialConfigure | Configures the serial port of the VT System channel. |
| SerialOpen vtsSerialOpen | Opens the serial port of the VT System channel. |
| SerialReceive vtsSerialReceive | Receives blocks of bytes from the serial port. |
| SerialSend vtsSerialSend | Sends a block of bytes to the serial port. |
| SetIntegrationTime vtsSetIntegrationTime | Sets the integration time for average values. |
| SetInterconnectionMode vtsSetInterconnectionMode | Sets the mode for interconnection of the three possible power supplies and the two power outputs of the power module VT7001. |
| SetMaxCurrentMode vtsSetMaxCurrentMode | Sets the mode for the control voltage output to control the power supply's maximal output current. |
| SetMinCurrentMeasurementRange vtsSetMinCurrentMeasurementRange | Sets the current measurement range that should be used from the automatic measuring range changeover of the VT7001 module. |
| SetRefVoltageMode vtsSetRefVoltageMode | Sets the mode for the reference voltage output to control the power supply's output voltage. |
| SerialSetOnErrorHandler vtsSerialSetOnErrorHandler | Sets the callback that notifies when an error occurred during a send or receive operation. |
| SerialSetOnReceiveHandler vtsSerialSetOnReceiveHandler | Sets the callback that notifies when data has been received on the serial port of the specified channel. |
| SerialSetOnSendHandler vtsSerialSetOnSendHandler | Sets the callback that notifies when a send operation on the serial port of the specified channel is completed successfully. |
| SetWFParams vtsSetWFParams | Configures the parameters for the output of a control voltage curve. |
| StartStimulation vtsStartStimulation | Starts stimulation output. |
| StopStimulation vtsStopStimulation | Stops stimulation output. |

| Methods/Functions | Short Description |
|---|---|
| vtsSetBackplaneRelay | Closes/opens the auxiliary relay on a connected VT backplane. |

| Version 15© Vector Informatik GmbH |
|---|
