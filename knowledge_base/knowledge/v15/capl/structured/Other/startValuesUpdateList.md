# startValuesUpdateList

> Category: `Other` | Type: `function`

## Syntax

```c
void startValuesUpdateList(); // form 1
void startValuesUpdateList(char groupName[]); // form 2
void startValuesUpdateList(char groupName[], long onlyActiveStartValues); // form 3
```

## Description

Sets the start values of variables/signals in the CANoeStart Value Window to the currently measured values.

## Parameters

| Name | Description |
|---|---|
| groupName | Name of a group containing start values. If groupName is defined, then only the active start values contained in this group get the currently measured values. If groupName is not defined or is equal to "", then only the active start values of all groups get the currently measured values. |
| onlyActiveStartValues | Determines if active start values get the currently measured values or not. If missing, then only the active start values are considered. 1 : Only the active start values get the currently measured values. 0: All start values (active and inactive) get the currently measured values. |

## Return Values

—

## Example

Example 1

Example 2

```c
on key '1'
{
  startValuesUpdateList("Start values group1");
}

on key '2'
{
  startValuesUpdateList();
}

on key '3'
{
  startValuesUpdateList(""); // corresponds to startValuesUpdateList();
}

on key '4'
{
  startValuesUpdateList("Start values group1", 1);
}

on stopMeasurement
{
  startValuesUpdateList();
}
variables
{
  msTimer t;
}
on timer t
{
  startValuesUpdateList();
}
on key '5'
{
  @myVariable = 123;

  //startValuesUpdateList();    // this call would not save the value 123 of myVariable
  //because the variable is set later than the function call is executed.


  setTimer(t, 0);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0: form 1-2 10.0 SP3: form 3 | 10.0: form 1-2 10.0 SP3: form 3 | 13.0 | — | 14 | 2.2: form 1-2 2.2 SP2: form 3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
