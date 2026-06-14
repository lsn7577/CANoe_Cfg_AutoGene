# SecurityLocalStartControlSimulationNode

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalStartControlSimulationNode(char nodeName[], char networkName[], dword orderNumber) // form 1
long SecurityLocalStartControlSimulationNode(char nodeId[], dword nodeIdType, char networkName[], dword orderNumber) // form 2
```

## Description

Registers the calling node to a node in the simulation setup. Both nodes require the SecMgrCANoeClient Nodelayer.

After a successful registration, the calling node can use all SecurityOfNode…() Functions to control the simulation node.

The calling node receives all OnSecurityOfNode… callbacks from the specified node on the specified network.

You have to call SecurityLocalStopControlSimulationNode to unregister.

Form 2 allows to control non-database simulation nodes.

## Parameters

| Name | Description |
|---|---|
| char nodeName[] | The name of the node to control. This refers to the name declared in the database. (Form 1) |
| char nodeId[] | The name or title of the node to control. Use either the node name of a network node declared in the database or the node title declared in the Simulation Setup of CANoe and set parameter nodeIdType accordingly. (Form 2) (see Simulation Setup: Network Node Configuration for further details on the difference between node title and node name) |
| dword nodeIdType | Configure how the parameter nodeId shall be interpreted. Possible Values: 1: nodeId refers to node name of a network node declared in the database 2: nodeId refers to node title declared in the Simulation Setup of CANoe (If Network Node is set to <<default>>) (Form 2) (see Simulation Setup: Network Node Configuration for further details on the difference between node title and node name) |
| dword nodeIdType | Configure how the parameter nodeId shall be interpreted. Possible Values: 1: nodeId refers to node name of a network node declared in the database 2: nodeId refers to node title declared in the Simulation Setup of CANoe (If Network Node is set to <<default>>) (Form 2) (see Simulation Setup: Network Node Configuration for further details on the difference between node title and node name) |
| char networkName[] | The name of the network the node to control is on. |
| dword orderNumber | Defines the position in the ordered list, in which the callbacks are executed. Order number 1 is reserved for the simulation node itself. Order number 2 means that the callback is triggered directly after the simulation node (number 1), but before any other node who may have registered to a higher order number. Only one node can register to an order number. If the order number is already used, the registration fails. |

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
| Since Version | — | 11.0 SP3: form 1 13.0: form 2 | 11.0 SP3: form 1 13.0: form 2 | — | — | — |
| Restricted To | — | CAN CAN FD FlexRay Ethernet | CAN CAN FD FlexRay Ethernet | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
