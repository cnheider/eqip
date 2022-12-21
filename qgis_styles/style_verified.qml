<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" simplifyDrawingTol="1" minScale="100000000" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="1" simplifyMaxScale="1" maxScale="0" labelsEnabled="0" simplifyAlgorithm="0" version="3.14.0-Pi" styleCategories="AllStyleCategories" simplifyLocal="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal endExpression="" accumulate="0" mode="0" fixedDuration="0" enabled="0" endField="" startField="" startExpression="" durationField="" durationUnit="min">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 forceraster="0" type="singleSymbol" symbollevels="0" enableorderby="0">
    <symbols>
      <symbol alpha="0.5" type="fill" name="0" force_rhr="0" clip_to_extent="1">
        <layer locked="0" enabled="1" class="SimpleFill" pass="0">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="105,117,196,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" name="name" value=""/>
              <Option name="properties"/>
              <Option type="QString" name="type" value="collection"/>
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
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory minScaleDenominator="0" diagramOrientation="Up" minimumSize="0" maxScaleDenominator="1e+8" spacingUnit="MM" penAlpha="255" opacity="1" barWidth="5" spacingUnitScale="3x:0,0,0,0,0,0" sizeScale="3x:0,0,0,0,0,0" scaleDependency="Area" penWidth="0" backgroundColor="#ffffff" direction="0" rotationOffset="270" showAxis="1" spacing="5" lineSizeType="MM" enabled="0" lineSizeScale="3x:0,0,0,0,0,0" labelPlacementMethod="XHeight" scaleBasedVisibility="0" penColor="#000000" backgroundAlpha="255" width="15" height="15" sizeType="MM">
      <fontProperties style="" description="Ubuntu,11,-1,5,50,0,0,0,0,0"/>
      <attribute color="#000000" label="" field=""/>
      <axisSymbol>
        <symbol alpha="1" type="line" name="" force_rhr="0" clip_to_extent="1">
          <layer locked="0" enabled="1" class="SimpleLine" pass="0">
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
                <Option type="QString" name="name" value=""/>
                <Option name="properties"/>
                <Option type="QString" name="type" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" obstacle="0" zIndex="0" showAll="1" linePlacementFlags="18" placement="1" priority="0">
    <properties>
      <Option type="Map">
        <Option type="QString" name="name" value=""/>
        <Option name="properties"/>
        <Option type="QString" name="type" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option type="Map" name="QgsGeometryGapCheck">
        <Option type="double" name="allowedGapsBuffer" value="0"/>
        <Option type="bool" name="allowedGapsEnabled" value="false"/>
        <Option type="QString" name="allowedGapsLayer" value=""/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <referencedLayers/>
  <referencingLayers/>
  <fieldConfiguration>
    <field name="DN">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" field="DN" name=""/>
    <alias index="1" field="id" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="DN" applyOnUpdate="0" expression=""/>
    <default field="id" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="DN" exp_strength="0"/>
    <constraint unique_strength="0" constraints="0" notnull_strength="0" field="id" exp_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint desc="" exp="" field="DN"/>
    <constraint desc="" exp="" field="id"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column type="field" hidden="0" name="id" width="-1"/>
      <column type="field" hidden="0" name="DN" width="-1"/>
      <column type="actions" hidden="1" width="-1"/>
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
    <field editable="1" name="DN"/>
    <field editable="1" name="id"/>
    <field editable="1" name="layer"/>
    <field editable="1" name="path"/>
  </editable>
  <labelOnTop>
    <field name="DN" labelOnTop="0"/>
    <field name="id" labelOnTop="0"/>
    <field name="layer" labelOnTop="0"/>
    <field name="path" labelOnTop="0"/>
  </labelOnTop>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>"id"</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
