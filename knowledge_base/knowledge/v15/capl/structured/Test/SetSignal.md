# SetSignal

> Category: `Test` | Type: `function`

## Syntax

```c
long setSignal(char signalName[], double aValue); // form 2
```

## Description

Sets the transmitted signal aSignal to the accompanying value.

If no suitable signal driver exists and thus no signal can be stimulated, then in the test module the verdict of the test module is set to "fail". In the modeling library the measurement is stopped and an error message is displayed.

## Parameters

| Name | Description |
|---|---|
| Note Signal Ambiguity You have to use further objects to identify the signal uniquely. They are: channel, database name (alias), node name and message name. The exact qualification syntax is:[Channel::][Database name (alias)::][Node::][Message::]Signal The order and completeness of the objects from right to left is important (see example). |  |
| aValue | Physical value to be accepted. |

## Example

Example 1 — Signal is unique

Example 2 — Signal is ambiguous

```c
setSignal("OnOff", 1.0);

//Message and signal
setSignal("LightState::OnOff", 1.0);
//Node, message and signal 
setSignal("LightSwitch::LightState::OnOff", 1.0);
//Database name (alias), node, message and signal 
setSignal("PowerTrain::LightSwitch::LightState::OnOff", 1.0);
setSignal("C11_Fy_Cluster::ESP::PDU_ESP_35::BTS_Bmg", 1);
//Channel, database name (alias), node, message and signal 
setSignal("CAN1::PowerTrain::LightSwitch::LightState::OnOff", 1.0);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | Test nodes | Test nodes | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
