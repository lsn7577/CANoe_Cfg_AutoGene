# MATLAB Integration CAPL Functions

> Category: `MATLAB` | Type: `notes`

## Description

The Simulink Coder generated DLL contains three additional functions which can be called by CAPL. These functions may be used to control the behavior of the generated CANoe MATLAB Integration and the execution of the Simulink model.

MATLAB Integration

| MATLAB Only available with MATLAB Integration Package. |
|---|

| Note The CANoe MATLAB Integration uses meaningful default values to set up and control Simulink model execution. These defaults are determined during the generation process by the Simulink Coder. If you use the CAPL functions described herein you can override these defaults and take control of model execution. |
|---|

| Note to Function Notation <ModelName> = placeholder for Simulink model |
|---|

| Functions | Short Description |
|---|---|
| <ModelName>_init | Initializes the CANoe runtime environment for the generated model DLL. |
| <ModelName>_step | Executes a simulation step. |
| GetSimulinkModelName | Returns the name of the Simulink model. |

| Version 15© Vector Informatik GmbH |
|---|
