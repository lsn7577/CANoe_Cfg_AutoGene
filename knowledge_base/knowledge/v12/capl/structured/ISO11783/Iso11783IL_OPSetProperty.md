# Iso11783IL_OPSetProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPSetProperty( char propertyName[], long newValue ); // form 1
```

## Description

The function sets a property of the Object Pool API, i.e. the supported Virtual Terminal version.

## Parameters

| Name | Description |
|---|---|
| Version | Supported version of the ISO11783 Virtual Terminal specification.Supported values: 2, 3 (default), 4 and 5If used, the version value obtained from the database (node attribute ISO11783OPVersion) is overwritten. |
| DebugLevel | Controls the output to the Write Window. Supported values: 0: No output 1: Only errors 2: Warnings and errors 3: Information, warnings and errors |
| SendPreferredAssignmentEvenIfEmpty | Enforces sending of the Preferred Assigning message to the Virtual Terminal, even if no of auxiliary function has a preferred assigned auxiliary input, i.e. the corresponding INI file (i.g. Sprayer.ini) contains following lines: [AuxAssignment]AuxAssignmentCount=0 Supported values: 0: Preferred Assigning message is sent to the Virtual Terminal if at least one preferred assignment exists 1: Preferred Assigning message is sent to the Virtual Terminal even if no preferred assignment exists |
| VTFunctionInstance | On startup the node connects to the Virtual Terminal (VT) which has this function instance. By default the node connects to the primary VT with function instance zero (0). If value -1 is used then the node connects to the first visible VT. |

## Return Values

0: Unction has been executed successfully

## Example

```c
Iso11783IL_OPSetProperty( "Version", 3 );
```

## Availability

| Since Version |
|---|
