# coTfs Test control functions

> Category: `CANopen` | Type: `notes`

## Description

Check

Parameter Control

Test Configurator

Test Control

InitializeTestSystem

This function can be used to set common test settings by calling simple test functions as follows.

SendCANMessage

This function sends a simple CAN frame by using the CAPL function output.

This function starts transmission of messages that produces a specified bus load. With the parameter baudRate and busTrafficCategory a definite CANoe log file is defined according to CiA® TR308. The message sequences of that file are replayed during measurement.

StopBackgroundBusload

This function calls CAPL function StopReplayFile to stop an active generation of bus load that has been started with StartBackgroundBusload.

UserDefinedFunction

This function calls the customizable CAPL test function. The customizable function may be defined in a separated CAPL file and this file can be inserted in the Include program section via the syntax #include.

coTfsSetSDOScan

See Also

| CANopen - Test Functions This section offers a brief overview of the additional functions for test control of the CANopen TFS node layer. To use the CAPL functions the node layer CANopenTfsNl.dll must be included. |
|---|

| Check Parameter Control | Test Configurator Test Control |
|---|---|

| Functions | Short Description |
|---|---|
| coTfsActivateGuardingReqMonitor | Checks the temporally correct occurrence of guarding RTRs and controls the corresponding callback functions. |
| coTfsActivateHeartbeatMonitor | Checks the temporally correct occurrence of the heartbeat producer message and calls the corresponding callback functions. |
| coTfsActivateSyncMonitor | Checks the temporally correct occurrence of the SYNC message and calls the corresponding callback functions. |
| coTfsActivateSyncPdoMonitor | Checks the temporally correct occurrence of SYNC PDO messages and calls the corresponding callback functions. |
| coTfsDeactivateGuardingReqMonitor | Switches off the checking of guarding RTRs. |
| coTfsDeactivateHeartbeatMonitor | Switches off the checking of the heartbeat producer. |
| coTfsDeactivateSyncMonitor | Switches off the checking of the SYNC messages. |
| coTfsDeactivateSyncPdoMonitor | Switches off the checking of the SYNC PDO messages. |

| Functions | Short Description |
|---|---|
| coTfsGetNodeId | Transfers the internally-stored node-ID. |
| coTfsSetNodeId | Sets the internally-stored node-ID. |
| coTfsSetSdoCANid | Sets the CAN identifier to be used for the SDO tests. |

| Note These functions are available in the ProCANopen Test Configurator only! |
|---|

| Functions | Short Description |
|---|---|
| InitializeTestSystem | This function can be used to set common test settings by calling simple test functions as follows. The functions coTfsSDOResetAbortList, coTfsSDOResetAccAbortList, coTfsEmcyResetList, and coTfsODClearAllEntries are executed if this function is called. The function coTfsNMTRequest is executed only if it is specified via the parameter sendNMTCmd. The functions coTfsSetNodeId, coTfsLoadDeviceDescription, coTfsSetTimeoutValue. and coTfsSetReportBehaviour are executed only if the function was not executed before or the respective parameter value has changed. |
| SendCANMessage | This function sends a simple CAN frame by using the CAPL function output. |
| StartBackgroundBusload | This function starts transmission of messages that produces a specified bus load. With the parameter baudRate and busTrafficCategory a definite CANoe log file is defined according to CiA® TR308. The message sequences of that file are replayed during measurement. |
| StopBackgroundBusload | This function calls CAPL function StopReplayFile to stop an active generation of bus load that has been started with StartBackgroundBusload. |
| TestWaitForTesterConfirmation | This function displays a window that shows the string to the tester. The tester can acknowledge the window with yes or no. |
| UserDefinedFunction | This function calls the customizable CAPL test function. The customizable function may be defined in a separated CAPL file and this file can be inserted in the Include program section via the syntax #include. |
| WriteTextInReport | This function writes the given text into report. |

| Functions | Short Description |
|---|---|
| coTfsArrToD | Converts a byte array to a dword value. |
| coTfsArrToQ | Converts a byte array to a qword value. |
| coTfsArrToW | Converts a byte array to a word value. |
| coTfsatoxD | Converts a string value in a dword value. |
| coTfsatoxL | Converts a string value in a long value. |
| coTfsClearObjectName | Deletes stored object names for a specific node or all nodes. |
| coTfsDToArr | Converts a dword value to a byte array. |
| coTfsGetApplProfile | Gets application profile. |
| coTfsGetTestModuleNodeId | Gets the node-ID of the tester. |
| coTfsGetVersion | Returns the version of the CANopen test feature set node layer. |
| coTfsLoadDeviceDescription | Reads an EDS, DCF or XML file to interpret objects index and sub index with object names in plain text. |
| coTfsResetTfs | Resets the CANopen TFS node layer. |
| coTfsSDOSetAbortControl | Defines which values are allowed for successful test completion. |
| coTfsSDOSetSdoAbortOnError | Enables or disables the sending of SDO abort codes on failed SDO accesses. |
| coTfsSetApplProfile | Sets application profile. |
| coTfsSetFailControl | Function that influences the report behavior of individual test functions. |
| coTfsSetReportBehaviour | Sets the report behavior of the CANopen TFS node layer. |
| coTfsSetTestModuleNodeId | Sets the node-ID of the tester. |
| coTfsSetTimeoutValue | Sets the general time-out for all test functions. |
| coTfsWToArr | Converts a word value to a byte array. |
| coTfsSetSDOScan | This functions performs a SDO upload of the mandatory object 0x1000 to detect if a CANopen® device is available. |

| Version 15© Vector Informatik GmbH |
|---|
