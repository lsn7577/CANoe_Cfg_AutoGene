# coTfsGetApplProfile

> Category: `CANopen` | Type: `function`

## Syntax

```c
dword coTfsGetApplProfile( void );
```

## Description

The function reads the currently set application profile.

## Return Values

Used application profile, 301 if not supported profile is used.

## Example

```c
dword appProfile;
                                
appProfile = coTfsGetApplProfile();
```
