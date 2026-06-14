# Diagnostics: Connection of the Communication Layer

> Category: `Diagnostics` | Type: `notes`

## Description

The diagnostic commands in CAPL allow access to the diagnostic services and data using symbols that were defined in the CANdela description file. For communication, this data must be transmitted, where two ways are available:

This interface may also be used in tester nodes and test modules if direct access to the transport protocol is necessary, e.g. to perform fault injection.

For connectionless transport protocols, Diag_SetupChannelCon can be called immediately.

Depending on the transport protocol implementation used, the events the CAPL program receives have to be forwarded to CANoe. Please refer to these functions for details:

A reference implementation of the CAPL Callback Interface in CANoe is available for the networks CAN, LIN, FlexRay (FlexRay TP AUTOSAR and FlexRay TP ISO) and DoIP/HSFZ using typical transport protocols for those bus systems.

For special applications in the course of ECU test and development those functions may be modified e.g. for inducing transmission errors for robustness tests (see online help OSEK TP (CAN Transport Protocol)).

The reference implementations are available as include files (*.cin) in the CANoe installation folder Reusable\CAPL_Includes\Diagnostics you find in the same directory like the CANoe sample configurations.

In order to use them, you simply need to do the following steps:

The following example shows a very simple CAPL ECU simulation node.

You may add additional on diagRequest <service> handlers for all diagnostic services you want to support with your simulation and change the value of gECU to the ECU qualifier you defined in the Diagnostics/ISO TP… dialog. Additionally, you might need to adapt the service name for the Tester Present service (in this example: TesterPresent_Process) to the service identifier specified in your diagnostic description:

includes{ // Include the CAPL Callback Interface (CCI) reference implementation for CAN TP #include "Diagnostics\CCI_CanTP.cin"}variables{ // Define constants necessary for the CCI reference implementation char gECU[20]="CAN_ECU"; // ECU qualifier defined in the // "Configuration|Diagnostics/ISO TP..." dialog int cIsTester=0; // This is a simulation node, no tester node}on preStart{ // Provide the link to the configured diagnostic description diagInitEcuSimulation(gECU);}// Very simple implementation of diagnostics services supported by this simulation// Only "Tester Present" is answered by a positive response, all other services by negative responseon diagRequest *{ diagResponse this resp; diagSendNegativeResponse(resp, 0x11); // Service not supported}on diagRequest TesterPresent_Process{ diagResponse this resp; diagSendPositiveResponse(resp);}

Expanded Functions in CAPL |Basic CAPL Procedure for an ECU Implementation | Basic CAPL Procedure for a Tester Implementation

| Version 15© Vector Informatik GmbH |
|---|
