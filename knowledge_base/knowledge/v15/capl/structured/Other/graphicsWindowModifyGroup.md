# graphicsWindowModifyGroup

> Category: `Other` | Type: `function`

## Syntax

```c
void graphicsWindowModifyGroup(char[] windowName, byte mode, char[] groupName);
```

## Description

Modifies group enabled and expanded states.

## Parameters

| Name | Description |
|---|---|
| windowName | The name of the Graphics Window. |
| byte mode | 1 = Enable group 2 = Disable group 3 = Expand group 4 = Collapse group 5 = Disable all groups 6 = Collapse all groups 7 = Expand all enabled groups 8 = Collapse all disabled groups |
| groupName | The name of the common axis/group to modify (optional parameter). |

## Return Values

—

## Example

```c
// Expand a group
graphicsWindowModifyGroup("Graphics", 3, "MyGroup");

// Disable all groups
graphicsWindowModifyGroup("Graphics", 5);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 SP3 | 12.0 SP3 | 13.0 | — | 14 | 4.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
