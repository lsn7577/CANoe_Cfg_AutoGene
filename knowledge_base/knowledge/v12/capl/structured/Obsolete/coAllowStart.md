# coAllowStart

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coAllowStart( dword errCode[] );
```

## Description

If a simulated node is configured as NMT master (Bit 0 in 1F80 set), there are various states during the start procedure in which the application is signaled by the event function coOnConfigReady. In these states, the simulated node waits for the release of the application in order to be able to continue the start procedure. The various events and the associated information can be read in the description of coOnConfigReady.

## Return Values

—

## Example

```c
void coOnConfigReady ( dword event, dword nodeId ){
  dword errCode[1];

  switch (event) {
    case 1:
      write( "Wait for start" );
      coAllowStart ( errCode );    // switch to operational
      break;
    case 4:
      write( "Software update state reached" );
      coAllowStart( errCode );    // go on with boot process by default
      break;
  };
}
```

## Availability

| Up to Version |
|---|
