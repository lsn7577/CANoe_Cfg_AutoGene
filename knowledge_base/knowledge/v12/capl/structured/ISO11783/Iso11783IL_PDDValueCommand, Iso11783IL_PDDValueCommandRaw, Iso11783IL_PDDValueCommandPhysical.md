# Iso11783IL_PDDValueCommand, Iso11783IL_PDDValueCommandRaw, Iso11783IL_PDDValueCommandPhysical

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDD ValueCommand (dword ddi, dword elementNumber); //form 1
```

## Description

Form (1) and (2) send the current value of the specified data entity to the Task Controller with Value command. It can be used to send to the Task Controller the previously set Compressed State DDIs (using Iso11783IL_PDDSetValueRaw or Iso11783IL_PDDSetValuePhysical).

Form (3)-(6) set the value to the specified data entity (if exists) and sends the value to the Task Controller with Value command.

## Example

```c
void ReportActualStateOfSomeSections()
{
  long result;

  // Sections 1, 3, 20 and 21 are enabled
  // All sections belong to the elementNumber=7
  //the first two sections belong to the DDI=161
  //the last two sections belong to the DDI=162
  Iso11783IL_PDDSetSectionState(Sprayer, 161, 7, 1, 1);
  Iso11783IL_PDDSetSectionState(Sprayer, 161, 7, 3, 1);
  Iso11783IL_PDDSetSectionState(Sprayer, 162, 7, 20, 1);
  Iso11783IL_PDDSetSectionState(Sprayer, 162, 7, 21, 1);

  //each DDI has to be sent with a single command
  //the first two sections belong to the DDI=161
  Iso11783IL_PDDValueCommand(Sprayer, 161, 7);
  //the last two sections belong to the DDI=162
  Iso11783IL_PDDValueCommand(Sprayer, 162, 7);
}
```

## Availability

| Since Version |
|---|
