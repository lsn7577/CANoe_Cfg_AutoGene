# TCIL_SetSectionState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_SetSectionState (dbNode client, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, dword sectionState); // form 1
```

## Description

These functions set the state of a single section without sending any command.

For the already specified DDIs (currently in range DDI=0 and DDI=520), the functions check if the sectionNumber fits to the DDI.

The corresponding DDI (with states of 16 sections) can be sent with the methods TCIL_ValueCommand/TCIL_ValueAndAckCommand.

## Return Values

0: Function has been executed successfully

## Example

```c
void EnableSomeSections ()
{
  long result;
  // Sections 1, 3, 20 and 21 has to be enabled
  // All sections belong to the elementNumber=7
  //the first two sections belong to the DDI=290
  //the last two sections belong to the DDI=291

  TCIL_SetSectionState(TC, Sprayer, 290, 7, 1, 1);
  TCIL_SetSectionState(TC, Sprayer, 290, 7, 3, 1);
  TCIL_SetSectionState(TC, Sprayer, 291, 7, 20, 1);
  TCIL_SetSectionState(TC, Sprayer, 291, 7, 21, 1);

  //each DDI has to be sent with a single command
  //the first two sections belong to the DDI=290
  TCIL_ValueCommand(TC, Sprayer, 290, 7);
  //the last two sections belong to the DDI=291
  TCIL_ValueCommand(TC, Sprayer, 291, 7);
}
```

## Availability

| Since Version |
|---|
