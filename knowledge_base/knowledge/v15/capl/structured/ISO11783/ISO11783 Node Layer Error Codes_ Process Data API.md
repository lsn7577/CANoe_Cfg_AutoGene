# ISO11783 Node Layer Error Codes: Process Data API

> Category: `ISO11783` | Type: `notes`

| Error Code | Description | Additional Parameterin Iso11783PDDOnError |
|---|---|---|
| 0 | OK - Function has been executed successfully. | — |
| -100 | General error - An unspecified error has occurred. | — |
| -101 | Invalid ECU handle - A function was given an invalid ECU handle. | — |
| -102 | Invalid parameter - A function was given an invalid parameter. | — |
| -103 | ECU handle is not a local ECU - The function needs an ECU handle of a local ECU. Local ECUs are created with Iso11783CreateECU(). | — |
| -104 | Invalid node layer context - A node layer function was not used in the right context. | — |

| Error Code | Description | Additional Parameterin Iso11783PDDOnError |
|---|---|---|
| -400 | Message cannot be sent | — |

| Error Code | Description | Additional Parameterin Iso11783PDDOnError |
|---|---|---|
| -600 | Process variable not found: an attempt was made to use a process variable that does not exist. | — |
| -601 | Task Controller not answering any more: the status message of the Task Controller is no longer received. | — |
| -602 | Invalid Data Log Command: the function Iso11783PDDSetLogTrigger has been called up with an invalid logging command. | — |
| -603 | A process variable could not be created. | — |
| -604 | Error while consistency check of the device description file: the device description file is invalid. | — |
| -605 | Action not valid in current state: the selected action could not be executed in the current state. | current state 0: not initialized, device description file not load 1: description file loaded, ready for initialization procedure 2: wait 6 seconds (start-up delay) 3: wait until task controller sends the status message 4: query information from the task controller 5: transfer device description 6: activate object pool 7: start up is complete 8: task is active |
| -606 | Version Request was not answered | — |
| -607 | Localization Label Request was not answered | — |
| -608 | Structure Label Request was not answered | — |
| -609 | Object Pool Transfer Request failed | — |
| -610 | Object Pool Transfer failed | — |
| -611 | Object Pool contains errors | — |
| -612 | Activation of Object Pool failed | — |
| -613 | The database attribute ISO11783PDDFilename is defined, but Process Data message is not in the Tx list. The device description will not be sent to the Task Controller or data logger. | — |
| -614 | The Process Data message is in the Tx list of a database node, but the attribute ISO11783PDDFilename is not defined. The device description will not be sent to the Task Controller. | — |
| -615 | The called function wants to access the Process Data Service of the node but in the current state it is not available. | — |
| -616 | A Task Controller or data logger reports an error in the Object Pool Delete message. | — |
| -617 | A message cannot be sent to the Task Controller because no Task Controller is detected in the network. | — |

| Version 15© Vector Informatik GmbH |
|---|
