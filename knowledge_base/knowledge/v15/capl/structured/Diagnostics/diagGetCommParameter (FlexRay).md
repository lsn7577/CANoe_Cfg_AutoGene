# diagGetCommParameter (FlexRay)

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetCommParameter (char qualifier[]);
```

## Description

Returns the value of a numeric/textual communication parameter of the given or currently active diagnostic description. The values are read from the diagnostic description if they cannot be set in the configuration dialog.

## Parameters

| Name | Description |
|---|---|
| Qualifier | Description |
| FlexRay.Protocol | The protocol variant to use. 0 AUTOSAR 2.xrest reserved for future extensions |
| Values |  |
| 1 | One byte addresses |
| 2 | Two byte addresses |
| FlexRay.LocalAddress | Address of *this* node, i.e. ECU address in ECU simulation, tester address in tester nodes. |
| FlexRay.RemoteAddress | Address of the target node, i.e. ECU address in tester nodes, tester address in ECU simulation. |
| Values |  |
| 1 | Unicast |
| 2 | Acknowledged Unicast |
| 3 | Acknowledged Unicast with Retry |
| rest | reserved |
| Note Please refer to the AUTOSAR FlexRay TP specification for details on the parameter value semantics. |  |
| Values |  |
| 1 | ISO |
| 2 | ISO6 |
| 3 | L16M |
| 4 | L4G |
| rest | reserved |
| Note Please refer to the AUTOSAR FlexRay TP specification for details on the parameter value semantics. |  |
| Note Please refer to the AUTOSAR FlexRay TP specification for details on the parameter value semantics. |  |
| Note Please refer to the AUTOSAR FlexRay TP specification for details on the parameter value semantics. |  |
| Qualifier | Description |
| FlexRay.LocalStartSlot | Id of first slot the node sends in |
| FlexRay.LocalCount | Number of consecutive slots to send in |
| FlexRay.LocalStartCycle | First cycle to send slots in |
| FlexRay.LocalCycleRepetition | Cycle spacing to send slots in |
| FlexRay.LocalPayloadLen | Length of slots to send in |
| FlexRay.RemoteStartSlot | Id of first slot to receive |
| FlexRay.RemoteCount | Number of consecutive slots to receive |
| FlexRay.RemoteStartCycle | First cycle to receive slots in |
| FlexRay.RemoteCycleRepetition | Cycle spacing of slots to receive |
| FlexRay.RemotePayloadLen | Length of slots received |

## Return Values

Error code

## Example

You can find examples for this function in the CAPL callback interface (CCI) reference implementations.See Diagnostics: Connection of the Communication Layer for details.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | — | — | — | 1.0 |
| Restricted To | — | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
