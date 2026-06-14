# Test Service Library: Commands to Control Checks

> Category: `Test` | Type: `notes`

## Description

In CAPL test modules it's recommended to use Checks as Constraints or Conditions and to create and start them straight before their usage (ChkStart_...).

testcase TC (){...chkid = ChkStart_MsgRelCycleTimeViolation (StatusMsg, 0.8, 1.2);TestAddConstraint (chkid);...TestRemoveConstraint (chkid);}

In this case there's no need to use Callback functions. In addition it's usually not necessary to query test results since violations of the test specification directly influence the test result and will be documented in the test report together with some relevant information.

In CAPL Simulation Nodes Checks can be used and controlled directly. In principle this works in CAPL test modules, too. Nevertheless it is not recommended and - apart from some rare special cases - there are no advantages in doing so.

You can define all checks "on_preStart" and use the control functions during a measurement to start/stop a check.

Checks may be stopped, (re-)started, reset and destroyed:

For test programs of typical size and duration, there is no necessity to destroy the checks in CAPL. Only those rare cases with extremely long running tests and dynamic check creation need to destroy checks to prevent a lack of memory.

For the check control there are the following functions to influence. These functions can be used to turn off checking in not relevant time (e.g. with changes of the network hardware), and to continue checking. These control functions can also be used to setup dependencies between checks:

| Functions | Short Description |
|---|---|
| ChkControl_Start | Begins or continues checking the event condition. |
| ChkControl_Stop | Turns off the checking of the event condition. |
| ChkControl_Reset | Initializes the status of the check. |
| ChkControl_Destroy | Destroys the check. |

| Version 15© Vector Informatik GmbH |
|---|
