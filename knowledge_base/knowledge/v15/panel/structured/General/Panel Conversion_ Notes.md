# Panel Conversion: Notes

> Category: `Panel` | Subcategory: `General` | Type: `concept`

Old panels are converted into the XVP format automatically by opening them in the Panel Designer. The target file obtains the same name as the source file, the save directory remains the same.

Note

Check the converted panels. It is possible that some panel settings could not be converted completely and would therefore not be carried over or were reset to their default values.

| Note Check the converted panels. It is possible that some panel settings could not be converted completely and would therefore not be carried over or were reset to their default values. |
|---|

## Information on Converting from the CNP Format to the XVP Format

If the conversion is unsuccessful or only partially successful, it may be caused by the following:

FAQ: The panel was saved with a very old version of the Panel Editor.

The panel must have a certain internal version so that it can be handled by the panel converter. The version number in the panel is issued when saving with the Panel Editor.

FAQ: The panel contains elements not supported by the Panel Designer.

The missing elements must be replaced manually.

FAQ: The panel contains invalid data.

The missing elements must be supplemented manually.

| FAQ: The panel was saved with a very old version of the Panel Editor. The panel must have a certain internal version so that it can be handled by the panel converter. The version number in the panel is issued when saving with the Panel Editor. |
|---|

| FAQ: The panel contains elements not supported by the Panel Designer. The missing elements must be replaced manually. |
|---|

| FAQ: The panel contains invalid data. The missing elements must be supplemented manually. |
|---|

## Conversion Rules

The most important conversion rules are listed below.

## Converting a Panel Editor Multi Display Control into a Panel Designer CAPL Output View

The Multi Display Control of the Panel Editor is converted into the CAPL Output View element of the Panel Designer.

The Multi Display Control can only display one output, which is overwritten by the next output. When the CAPL Output View element is generated, it exhibits the same behavior, i.e. the Output Mode property is set to Overwrite.

## Converting a Panel Editor Clock Control into a Panel Designer Clock Control

The Clock Control of the Panel Editor is converted into the Clock Control of the Panel Designer.

The following use cases for the Panel Editor control are converted:

The following Panel Editor use cases are not converted, i.e. no new Clock Control is generated:
