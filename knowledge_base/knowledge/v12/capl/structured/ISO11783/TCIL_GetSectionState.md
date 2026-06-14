# TCIL_GetSectionState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetSectionState (dbNode client, dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, dword& sectionState); // form 1
```

## Description

These functions return the current state of a single section.

For the already specified DDIs (currently in range DDI=0 and DDI=520), the functions check if the sectionNumber fits to the DDI.

## Return Values

0: Function has been executed successfully

## Example

```c
dword IsSectionEnabled(dword elementNumber, dword sectionNumber)
{
  long result;
  dword state;
  result = TCIL_GetSectionState(TC, Sprayer, 161, elementNumber, sectionNumber, state);
  if (result < 0)
  {
    TestStepFail("Failed to get current state!");
    return result;
  }
  return (state == 1);
}
```

## Availability

| Since Version |
|---|
