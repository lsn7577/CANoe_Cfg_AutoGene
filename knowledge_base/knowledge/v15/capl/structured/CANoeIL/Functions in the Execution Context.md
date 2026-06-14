# Functions in the Execution Context

> Category: `CANoeIL` | Type: `notes`

| Node Context in theSimulation Setup The interaction layer is generally executed in the node context. This means that the CAPL interface can be used only within this node. In this way it is ensured that the relationship between a node and its model is maintained. | Global Functions in theSimulation Setup Various control and disturbance functions are provided for implementing a central control node in the Simulation Setup. | Functions in theTest Module Various control and disturbance functions are provided for implementing tests in the CAPL test module. |
|---|---|---|
| ILActivateClamp15 | — | — |
| ILDeactivateClamp15 | — | — |
| ILControlInit | — | — |
| ILControlStart | — | — |
| ILControlStop | — | — |
| ILControlWait | — | — |
| ILControlResume | — | — |
| ILControlSimulationOff | — | — |
| ILControlSimulationOn | — | — |
| ILErrno | — | — |
| ILSetResultString | — | — |
| ILFaultInjectionDisableMsg | ILDisableMSG | TestDisableMsg |
| ILFaultInjectionEnableMsg | ILEnableMSG | TestEnableMsg |
| ILFaultInjectionResetAllFaultInjections | — | TestResetAllFaultInjections |
| ILFaultInjectionResetMsgCycleTime | — | TestResetMsgCycleTime |
| ILFaultInjectionResetMsgDlc | — | TestResetMsgDlc |
| ILFaultInjectionSetMsgDlc | — | TestSetMsgDlc |
| ILFaultInjectionSetMsgCycleTime | — | TestSetMsgCycleTime |
| ILSetMsgEvent | — | TestSetMsgEvent |

| Version 15© Vector Informatik GmbH |
|---|
