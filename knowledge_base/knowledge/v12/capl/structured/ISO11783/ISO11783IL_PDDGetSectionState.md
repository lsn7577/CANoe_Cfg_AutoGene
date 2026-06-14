# ISO11783IL_PDDGetSectionState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long ISO11783IL_PDDGetSectionState(dword ddiOfCondensedState, dword elementNumber, dword sectionNumber); // form 1
```

## Description

Returns the current state of a single section.

For the already specified DDIs (currently in range DDI=0 and DDI=520), the functions check if the sectionNumber fits to the DDI.

## Return Values

0: disabled/off

## Example

```c
long value;
char text[256];
value = Iso11783IL_PDDGetSectionState(290, 10, 1);
if (value < 0)
{
  Iso11783IL_GetLastErrorText( elCount(text), text );
  write( "ERROR: %s", text);
}
```

## Availability

| Since Version |
|---|
