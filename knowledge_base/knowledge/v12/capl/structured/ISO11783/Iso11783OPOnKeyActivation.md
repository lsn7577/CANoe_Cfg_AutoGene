# Iso11783OPOnKeyActivation

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783OPOnKeyActivation( dword ecuHandle, dword objectID, dword parentID, dword keyCode, dword activation );
```

## Description

The function is called by the node layer, if the user presses a soft key or button.

## Return Values

—

## Example

```c
void Iso11783OPOnKeyActivation( dword handle, dword object ID, dword parentID, dword keyCode, 
 dword activation )
{
  if (activation == 1) {
    switch(keyCode) {
    case 1: DoSometing1(); break;
    case 2: DoSometing2(); break;
    }
  }
}
```

## Availability

| Since Version |
|---|
