# <ModelName>_init

> Category: `MATLAB` | Type: `function`

## Syntax

```c
long <ModelName>_init( dword enableTimer, dword enableEvents);
```

## Description

Initializes the CANoe runtime environment for the generated model DLL. This effectively overrides the default execution settings which were compiled into the DLL.

## Parameters

| Name | Description |
|---|---|
| enableTimer | Enables or disables the internal model execution timer. Per default the generated Simulink model is executed by the CANoe runtime environment according to its fixed simulation step size. If the user sets the fixed step size to auto, Simulink calculates the required minimum fixed step size based on the model contents. However, if the user specifies a fixed step size Simulink checks this value against the model contents during simulation start-up and generates an error message if the step size violates any timing restrictions. If the Simulink model is built into a DLL with the Simulink Coder, the fixed step size is written into the generated C source code (see generated MdlInitializeSampleTimes function in <ModelName>.c). The CANoe MATLAB Integration reads this generated fixed step size value during measurement start-up to set up a timer used to execute the model at the specified sample time, thus providing exactly the same execution environment as in Simulink. If the user wants to execute the model non-cyclically at arbitrary sample times (for example with the <ModelName>_step function) the user must disable the CANoe MATLAB Integration timer. This is done by setting this parameter to zero. |
| enableEvents | Enables or disables the event triggered model execution. In addition (or instead) of using the <ModelName>_step function to execute the model a simulation step may be performed on each environment variable change. To activate this feature this parameter must be set to a nonzero value. |

## Return Values

On success 0, otherwise a value unequal to zero.

## Example

```c
on start
{
modelTimer.SetCyclic(myTimeStep);
myControllerMdl_init(0,1);
}
```

## Availability

- Availability
