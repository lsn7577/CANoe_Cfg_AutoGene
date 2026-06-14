# Iso11783FSMove

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783FSMove( char sourcePath[], char destPath[], dword movemode );
```

## Description

The function moves, copies or deletes a file or directory.

## Return Values

0 or error code

## Example

```c
// Move
Iso11783FSMove( "\TEST.TXT", "\DIR1\TEST.TXT", 0x00 
 );

// Copy & Rename
Iso11783FSMove( "\TEST.TXT", "\DIR1\TEST2.TXT", 0x01 
 );

// Delete (even, if "TEST.TXT" 
 is read-only)
Iso11783FSMove( "\TEST.TXT", 0, 0x06 );
```

## Availability

| Since Version |
|---|
