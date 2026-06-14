# getSignal

> Category: `Test` | Type: `function`

## Syntax

```c
float getSignal(char signalName[]); // form 2
```

## Description

Gets the value of a signal.

## Parameters

| Name | Description |
|---|---|
| Note Signal Ambiguity You have to use further objects to identify the signal uniquely. They are: channel, database name (alias), node name and message name. The exact qualification syntax is:[Channel::][Database name (alias)::][Node::][Message::]Signal The order and completeness of the objects from right to left is important (see example). |  |

## Return Values

Value of the signal; 0.0 if the signal is not found.

## Example

Example 1 — Signal is unique

Example 2 — Signal is ambiguous

```c
float value;
value = getSignal("OnOff");

float value;
//Message and signal
value = getSignal("LightState::OnOff");
//Node, message and signal 
value = getSignal("LightSwitch::LightState::OnOff");
//Database name (alias), node, message and signal 
value = getSignal("PowerTrain::LightSwitch::LightState::OnOff");
value = getSignal("C11_Fy_Cluster::ESP::PDU_ESP_35::BTS_Bmg");
//Channel, database name (alias), node, message and signal 
value = getSignal("CAN1::PowerTrain::LightSwitch::LightState::OnOff");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
