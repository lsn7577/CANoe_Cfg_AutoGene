# SecurityLocalStopControlSimulationNode

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalStopControlSimulationNode(char nodeName[], char networkName[]) // form 1
long SecurityLocalStopControlSimulationNode(char nodeId[], dword nodeIdType, char networkName[]) // form 2
```

## Description

Stops controlling (deregistration) the specified simulation node on the specified network.

After a successful deregistration, you cannot call any SecurityOfNode…() functions at the previously registered node, neither you will receive any OnSecurityOfNode… callbacks.

You have to call SecurityLocalStartControlSimulationNode to register.

## Parameters

| Name | Description |
|---|---|
| char nodeName[] | The name of the node to deregister from. This refers to the name declared in the database. (Form 1) |
| char nodeId[] | The name or title of the node to deregister from. Use either the node name of a network node declared in the database or the node title declared in the Simulation Setup of CANoe and set parameter nodeIdType accordingly. (Form 2) (see Simulation Setup: Network Node Configuration for further details on the difference between node title and node name) |
| dword nodeIdType | Configure how the parameter nodeId shall be interpreted. Possible Values: 1: nodeId refers to node name of a network node declared in the database 2: nodeId refers to node title declared in the Simulation Setup of CANoe (If Network Node is set to <<default>>) (Form 2) (see Simulation Setup: Network Node Configuration for further details on the difference between node title and node name) |
| char networkName[] | The name of the network the node to deregister from is on. |

## Return Values

A Value of 1 means that the action was successful. A value less than or equal to 0 means error. A value larger than 1 means warning.

## Example

```c
//form 1
on start
{
  dword result = 0;
  result = SecurityLocalStartControlSimulationNode("DatabaseNode", "CAN", 2);
  Write("SecurityLocalStartControlSimulationNode for network node with name DatabaseNode returned %i", result);
}

on stopMeasurement
{
  dword result = 0;
  result = SecurityLocalStopControlSimulationNode("DatabaseNode", "CAN");
  Write("SecurityLocalStopControlSimulationNode for network node with name DatabaseNode returned %i", result);
}

//form 2
on start
{
  dword result = 0;
  result = SecurityLocalStartControlSimulationNode("MyNode", 2, "CAN", 2); //Use the node title, if the node is not declared in the database (Network Node is set to <<default>>)
  Write("SecurityLocalStartControlSimulationNode for node with title MyNode returned %i", result);
}

on stopMeasurement
{
  dword result = 0;
  result = SecurityLocalStopControlSimulationNode("MyNode", 2, "CAN"); //Use the node title, if the node is not declared in the database (Network Node is set to <<default>>)
  Write("SecurityLocalStopControlSimulationNode for node with title MyNode returned %i", result);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP3: form 1 13.0: form 1 | 11.0 SP3: form 1 13.0: form 1 | — | — | — |
| Restricted To | — | CAN CAN FD FlexRay Ethernet | CAN CAN FD FlexRay Ethernet | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
