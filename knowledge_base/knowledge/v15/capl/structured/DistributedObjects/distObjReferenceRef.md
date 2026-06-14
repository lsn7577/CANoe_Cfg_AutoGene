# distObjReferenceRef

> Category: `DistributedObjects` | Type: `function`

## Syntax

```c
distObjReferenceRef *
distObjReferenceRef <Interface>
```

## Description

References a reference to a distributed object that is derived from the given interface.

## Parameters

| Name | Description |
|---|---|
| Interface | The optionally qualified name of a distributed object interface. It is also possible to take the reverse of in interface by using the reverse<…> operator. |

## Example

```c
// vCDL
version 1.3;
namespace SomeNamespace {
  interface SomeInterface {
    internal data int32 d;
  }
  object Obj : SomeInterface {}
  reference<SomeInterface> Ref;
}

// CAPL
on start {
  UseVariable();
  AccessTarget();
  AccessMember();
}

void UseVariable() {
  // variable declarations
  distObjReferenceRef * r1;
  distObjReferenceRef SomeInterface r2 = Ref;

  // check if a valid reference is referenced
  write("%d", r1.IsValid); // output: 0
  write("%d", r2.IsValid); // output: 1

  // type conversions (checked at runtime)
  r1 = r2;                                    // implicit upcast
  r2 = (distObjReferenceRef SomeInterface)r1; // explicit downcast

  // check the name and path of the reference
  write("%s", r1.Name); // output: Ref
  write("%s", r1.Path); // output: SomeNamespace::Ref
}

void AccessTarget() {
  // set the target directly (not possible at wildcard reference)
  Ref.SetTarget(Obj);

  // reset the target
  Ref.ResetTarget();

  // reset the target with empty string
  Ref.SetTargetByPath("");

  // set the target via its fully qualified path
  Ref.SetTargetByPath("SomeNamespace::Obj");

  // check if the reference target is valid
  write("%d", Ref.HasTarget);      // output: 1
  write("%d", Ref.Target.IsValid); // output: 1

  // access the reference target path
  write("%s", $Ref.TargetPath); // output: SomeNamespace::Obj
  write("%s", Ref.Target.Path); // output: SomeNamespace::Obj
}

void AccessMember() {
  // set the member at the reference
  $Ref.d = 42;
  write("%d = %d", $Obj.d, $Ref.d); // output: 42 = 42
}

on value_update Ref.TargetPath {
  write("Target of Ref was updated to: \"%s\"", $this);
}
on value_change Ref.TargetPath {
  write("Target of Ref was changed to: \"%s\"", $this);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | 14 | 15 | 14 | 5.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
