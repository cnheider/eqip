<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" minScale="100000000" labelsEnabled="0" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1" version="3.14.0-Pi" simplifyAlgorithm="0" simplifyDrawingTol="1" simplifyLocal="1" maxScale="0" simplifyMaxScale="1" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal mode="0" fixedDuration="0" startField="" endField="" durationUnit="min" accumulate="0" enabled="0" durationField="" endExpression="" startExpression="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 type="singleSymbol" symbollevels="0" enableorderby="0" forceraster="0">
    <symbols>
      <symbol type="fill" alpha="1" force_rhr="0" name="0" clip_to_extent="1">
        <layer locked="0" class="SimpleLine" pass="0" enabled="1">
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="53,121,177,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.96" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory scaleDependency="Area" backgroundColor="#ffffff" scaleBasedVisibility="0" opacity="1" height="15" lineSizeType="MM" spacingUnit="MM" minScaleDenominator="0" labelPlacementMethod="XHeight" barWidth="5" rotationOffset="270" sizeScale="3x:0,0,0,0,0,0" maxScaleDenominator="1e+8" direction="0" minimumSize="0" enabled="0" diagramOrientation="Up" sizeType="MM" penAlpha="255" penWidth="0" penColor="#000000" backgroundAlpha="255" spacingUnitScale="3x:0,0,0,0,0,0" showAxis="1" width="15" spacing="5" lineSizeScale="3x:0,0,0,0,0,0">
      <fontProperties style="" description="Ubuntu,11,-1,5,50,0,0,0,0,0"/>
      <axisSymbol>
        <symbol type="line" alpha="1" force_rhr="0" name="" clip_to_extent="1">
          <layer locked="0" class="SimpleLine" pass="0" enabled="1">
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings obstacle="0" zIndex="0" showAll="1" placement="1" priority="0" dist="0" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option type="Map" name="QgsGeometryGapCheck">
        <Option type="double" value="0" name="allowedGapsBuffer"/>
        <Option type="bool" value="false" name="allowedGapsEnabled"/>
        <Option type="QString" value="" name="allowedGapsLayer"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <referencedLayers/>
  <referencingLayers/>
  <fieldConfiguration>
    <field name="id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="DN">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="layer">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="path">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="id" name="" index="0"/>
    <alias field="DN" name="" index="1"/>
    <alias field="layer" name="" index="2"/>
    <alias field="path" name="" index="3"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="id" expression="" applyOnUpdate="0"/>
    <default field="DN" expression="" applyOnUpdate="0"/>
    <default field="layer" expression="" applyOnUpdate="0"/>
    <default field="path" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint field="id" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="DN" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="layer" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
    <constraint field="path" unique_strength="0" constraints="0" notnull_strength="0" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="id" exp="" desc=""/>
    <constraint field="DN" exp="" desc=""/>
    <constraint field="layer" exp="" desc=""/>
    <constraint field="path" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" sortExpression="" actionWidgetStyle="dropDown">
    <columns>
      <column hidden="0" type="field" width="-1" name="id"/>
      <column hidden="0" type="field" width="-1" name="DN"/>
      <column hidden="0" type="field" width="-1" name="layer"/>
      <column hidden="0" type="field" width="-1" name="path"/>
      <column hidden="1" type="actions" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="DN" editable="1"/>
    <field name="id" editable="1"/>
    <field name="layer" editable="1"/>
    <field name="path" editable="1"/>
  </editable>
  <labelOnTop>
    <field labelOnTop="0" name="DN"/>
    <field labelOnTop="0" name="id"/>
    <field labelOnTop="0" name="layer"/>
    <field labelOnTop="0" name="path"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"id"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
