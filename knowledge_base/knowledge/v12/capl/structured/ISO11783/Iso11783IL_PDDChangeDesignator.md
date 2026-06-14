# Iso11783IL_PDDChangeDesignator

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDChangeDesignator( word objectID, char asciiDesignator[] ); // form 1
```

## Description

The function sends a Change Designator message with a new object designator to the Task Controller.

The first variant converts the ASCII designator string to an UTF-8 string if the supported version is 2 or higher.

In the second variant you can specify if the designator string shall encoded to UTF-8 or not.

## Return Values

error code

## Example

```c
if (Iso11783IL_PDDChangeDesignator (1, "myNewDesignator" ) == 0) {
  write( "Change Designator command is sent successfully" );
}
char euroSign[255];
euroSign.byte(0) = 0xE2;
euroSign.byte(1) = 0x82;
euroSign.byte(2) = 0xAC;
euroSign.byte(3) = 0;

if (Iso11783IL_PDDChangeDesignator ( 1, euroSign, 0 ) == 0) {
  write( "Command to change designator to '€' is sent successfully" );
}
```

## Availability

| Since Version |
|---|
