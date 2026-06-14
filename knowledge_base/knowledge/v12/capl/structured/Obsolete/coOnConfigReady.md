# coOnConfigReady

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coOnConfigReady( dword event, dword nodeId );
```

## Description

During the start, a simulated node as configuration manager can supply other nodes on the network with configuration data. This data is then transmitted via SDO by the simulated configuration manager. The function informs the user about the current state of the configuration process.

## Return Values

—

## Example

```c
void coOnConfigReady( 
 dword event, dword nodeId ){

  dword 
 errCode[1];

  switch 
 (event) {
    case 
 0:
      write( 
 "Configuration management started" );
      break;
    case 
 1:
      write( 
 "Wait for start" );
      break;
    case 
 2:
      write( 
 "All mandatory nodes configured" );
      break;
    case 
 3:
      if 
 (nodeId) {
        write( 
 "Node %d configured", nodeId );
      }
      else 
 {
        write( 
 "All nodes configured" );
      }
      break;
    case 
 4:
      write( 
 "Software update state reached" );
      coAllowStart(errCode); 
    // go on with boot process by default
      break;
    case 5: 
      write( "Output level set differing from default" );
      break;
    case 6:
      write( "Mandatory node fails error control - NMT reset all nodes transmitted" );
      break;
    case 7:
      write( "Mandatory node fails error control - NMT stop all nodes transmitted" );
      break;
  };
}
```

## Availability

| Up to Version |
|---|
