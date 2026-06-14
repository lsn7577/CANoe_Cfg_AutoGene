# enableControl

> Category: `Other` | Type: `function`

## Syntax

```c
void enableControl(char panel[], char control[], long enable);
```

## Description

Selective activation and deactivation of the following elements:

If a control and display element is configured as a simple display, this command will have no effect on the element in question.The turned on or turned off state of an element remains intact at the start/end of the measurement. Because of this, a defined state should be created for the beginning of the measurement for the elements involved (for example in the CAPL program under System->Start).

## Return Values

—

## Example

```c
on key 'a'
{
enableControl("gateway", "ElemPanelHelp", 1);
// Activates Panel help in the "gateway" panel.
// enable all controls of the panel
enableControl("gateway", "", 1);
}
```

## Availability

| Since Version |
|---|
