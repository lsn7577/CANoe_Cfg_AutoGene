# SymbolMappingSetDynamicGroup

> Category: `Obsolete` | Type: `notes`

## Description

Name of a dynamic set which shall be activated.

| Deprecated Function Replaced by SymbolMappingSetDynamicMappingSet. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | void SymbolMappingSetDynamicGroup(char mappingSetName[]); |  |  |  |
| Function | Changes the dynamic mapping set that will be used for mapping in the CANoe Symbol Mapping dialog. Only the mapping relations contained in the given dynamic mapping set and in the static mapping set are considered. |  |  |  |
| Parameters | mappingSetName Name of a dynamic set which shall be activated. |  |  |  |
| Return Values | — |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 11.0 - 11.0 SP2 | — | — | • |  |
| Example on key '3'{ // Activate RT 3 and map RT 3 SymbolMappingSetDynamicGroup("RT 3");}on key '4'{ // Activate RT 4 and map RT 4 SymbolMappingSetDynamicGroup("RT 4");} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
