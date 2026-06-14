# Iso11783IL_OPGetVersion

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPGetVersion( ); // form 1
```

## Description

The function requests the stored object pools from the Virtual Terminal. A Get Version command or a Get Extended Version command is sent to the Virtual Terminal. If a response from the Virtual Terminal is received, the callback function Iso11783IL_OPOnResponse is called.

## Example

```c
Iso11783IL_OPGetVersion( 
);

[...]

void Iso11783IL_OPOnResponse( dword handle, pg VTtoECU 
 response ) {
  switch(response.BYTE(0)) {
  case 224:
    // handle GetVersion response here
    break;
  case 211:
    // handle Get Extended Version response here
    break;
  }
}
```

## Availability

| Since Version |
|---|
