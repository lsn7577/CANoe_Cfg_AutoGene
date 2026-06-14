# ISO11783IL_PDDSetSectionState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long ISO11783IL_PDDSetSectionState(dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, dword sectionState); // form 1
```

## Description

Sets the state of a single section.

For the already specified DDIs (currently in range DDI=0 and DDI=520), the functions check if the sectionNumber fits to the DDI.

## Return Values

0: function has been executed successfully

## Example

```c
long result;
char text[256];
result = Iso11783IL_PDDSetSectionState(290, 10, 1, 1);
if (result < 0)
{
  Iso11783IL_PDDGetLastErrorText ( elCount(text), text );
  write( "ERROR: %s", text);
}
```

## Availability

| Since Version |
|---|
