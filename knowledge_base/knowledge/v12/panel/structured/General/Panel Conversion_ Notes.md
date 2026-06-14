# Panel Conversion: Notes

> Category: `Panel` | Subcategory: `General` | Type: `concept`

You can use the Panel Designer's Import function to convert Panel Editor panels (CNP files) into Panel Designer panels (XVP files).

The most important conversion rules are listed below.

## Converting a Panel Editor Multi Display Control into a Panel Designer CAPL Output View

The Multi Display Control of the Panel Editor is converted into the CAPL Output View element of the Panel Designer.

The Multi Display Control can only display one output, which is overwritten by the next output. When the CAPL Output View element is generated, it exhibits the same behavior, i.e. the Output Mode property is set to Overwrite.

## Converting a Panel Editor Clock Control into a Panel Designer Clock Control

The Clock Control of the Panel Editor is converted into the Clock Control of the Panel Designer.

The following use cases for the Panel Editor control are converted:

The following Panel Editor use cases are not converted, i.e. no new Clock Control is generated:
