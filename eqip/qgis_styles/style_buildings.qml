<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="100000000" readOnly="0" hasScaleBasedVisibilityFlag="0" simplifyMaxScale="1" simplifyAlgorithm="0" simplifyLocal="1" styleCategories="AllStyleCategories" maxScale="0" labelsEnabled="0" simplifyDrawingHints="1" version="3.12.3-București" simplifyDrawingTol="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" symbollevels="0" type="singleSymbol" forceraster="0">
    <symbols>
      <symbol clip_to_extent="1" name="0" alpha="1" force_rhr="0" type="fill">
        <layer enabled="1" locked="0" pass="0" class="SimpleFill">
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="131,51,54,255" k="color"/>
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
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory width="15" scaleBasedVisibility="0" lineSizeType="MM" labelPlacementMethod="XHeight" diagramOrientation="Up" showAxis="1" spacing="5" spacingUnit="MM" sizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" minimumSize="0" sizeType="MM" rotationOffset="270" minScaleDenominator="0" backgroundAlpha="255" scaleDependency="Area" opacity="1" penColor="#000000" penWidth="0" height="15" barWidth="5" direction="0" enabled="0" spacingUnitScale="3x:0,0,0,0,0,0" maxScaleDenominator="1e+8" lineSizeScale="3x:0,0,0,0,0,0" penAlpha="255">
      <fontProperties description="Ubuntu,11,-1,5,50,0,0,0,0,0" style=""/>
      <axisSymbol>
        <symbol clip_to_extent="1" name="" alpha="1" force_rhr="0" type="line">
          <layer enabled="1" locked="0" pass="0" class="SimpleLine">
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
                <Option name="name" value="" type="QString"/>
                <Option name="properties"/>
                <Option name="type" value="collection" type="QString"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" showAll="1" priority="0" obstacle="0" linePlacementFlags="18" placement="1" zIndex="0">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option name="QgsGeometryGapCheck" type="Map">
        <Option name="allowedGapsBuffer" value="0" type="double"/>
        <Option name="allowedGapsEnabled" value="false" type="bool"/>
        <Option name="allowedGapsLayer" value="" type="QString"/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <referencedLayers/>
  <referencingLayers/>
  <fieldConfiguration>
    <field name="FOT_ID">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="MOB_ID">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="FEAT_KODE">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="FEAT_TYPE">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="FEATSTATUS">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="GEOMSTATUS">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="BBRAKTION">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="BYGN_TYPE">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="BYGN_UUID">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="METODE_3D">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="MAALESTED">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="UNDER_MIN">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="TIMEOF_CRE">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="TIMEOF_PUB">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="TIMEOF_REV">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="TIMEOF_EXP">
      <editWidget type="DateTime">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" name="" field="FOT_ID"/>
    <alias index="1" name="" field="MOB_ID"/>
    <alias index="2" name="" field="FEAT_KODE"/>
    <alias index="3" name="" field="FEAT_TYPE"/>
    <alias index="4" name="" field="FEATSTATUS"/>
    <alias index="5" name="" field="GEOMSTATUS"/>
    <alias index="6" name="" field="BBRAKTION"/>
    <alias index="7" name="" field="BYGN_TYPE"/>
    <alias index="8" name="" field="BYGN_UUID"/>
    <alias index="9" name="" field="METODE_3D"/>
    <alias index="10" name="" field="MAALESTED"/>
    <alias index="11" name="" field="UNDER_MIN"/>
    <alias index="12" name="" field="TIMEOF_CRE"/>
    <alias index="13" name="" field="TIMEOF_PUB"/>
    <alias index="14" name="" field="TIMEOF_REV"/>
    <alias index="15" name="" field="TIMEOF_EXP"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default expression="" applyOnUpdate="0" field="FOT_ID"/>
    <default expression="" applyOnUpdate="0" field="MOB_ID"/>
    <default expression="" applyOnUpdate="0" field="FEAT_KODE"/>
    <default expression="" applyOnUpdate="0" field="FEAT_TYPE"/>
    <default expression="" applyOnUpdate="0" field="FEATSTATUS"/>
    <default expression="" applyOnUpdate="0" field="GEOMSTATUS"/>
    <default expression="" applyOnUpdate="0" field="BBRAKTION"/>
    <default expression="" applyOnUpdate="0" field="BYGN_TYPE"/>
    <default expression="" applyOnUpdate="0" field="BYGN_UUID"/>
    <default expression="" applyOnUpdate="0" field="METODE_3D"/>
    <default expression="" applyOnUpdate="0" field="MAALESTED"/>
    <default expression="" applyOnUpdate="0" field="UNDER_MIN"/>
    <default expression="" applyOnUpdate="0" field="TIMEOF_CRE"/>
    <default expression="" applyOnUpdate="0" field="TIMEOF_PUB"/>
    <default expression="" applyOnUpdate="0" field="TIMEOF_REV"/>
    <default expression="" applyOnUpdate="0" field="TIMEOF_EXP"/>
  </defaults>
  <constraints>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="FOT_ID" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="MOB_ID" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="FEAT_KODE" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="FEAT_TYPE" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="FEATSTATUS" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="GEOMSTATUS" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="BBRAKTION" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="BYGN_TYPE" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="BYGN_UUID" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="METODE_3D" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="MAALESTED" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="UNDER_MIN" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="TIMEOF_CRE" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="TIMEOF_PUB" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="TIMEOF_REV" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="TIMEOF_EXP" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="FOT_ID" desc=""/>
    <constraint exp="" field="MOB_ID" desc=""/>
    <constraint exp="" field="FEAT_KODE" desc=""/>
    <constraint exp="" field="FEAT_TYPE" desc=""/>
    <constraint exp="" field="FEATSTATUS" desc=""/>
    <constraint exp="" field="GEOMSTATUS" desc=""/>
    <constraint exp="" field="BBRAKTION" desc=""/>
    <constraint exp="" field="BYGN_TYPE" desc=""/>
    <constraint exp="" field="BYGN_UUID" desc=""/>
    <constraint exp="" field="METODE_3D" desc=""/>
    <constraint exp="" field="MAALESTED" desc=""/>
    <constraint exp="" field="UNDER_MIN" desc=""/>
    <constraint exp="" field="TIMEOF_CRE" desc=""/>
    <constraint exp="" field="TIMEOF_PUB" desc=""/>
    <constraint exp="" field="TIMEOF_REV" desc=""/>
    <constraint exp="" field="TIMEOF_EXP" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortExpression="" sortOrder="0">
    <columns>
      <column name="FOT_ID" width="-1" type="field" hidden="0"/>
      <column name="MOB_ID" width="-1" type="field" hidden="0"/>
      <column name="FEAT_KODE" width="-1" type="field" hidden="0"/>
      <column name="FEAT_TYPE" width="-1" type="field" hidden="0"/>
      <column name="FEATSTATUS" width="-1" type="field" hidden="0"/>
      <column name="GEOMSTATUS" width="-1" type="field" hidden="0"/>
      <column name="BBRAKTION" width="-1" type="field" hidden="0"/>
      <column name="BYGN_TYPE" width="-1" type="field" hidden="0"/>
      <column name="BYGN_UUID" width="-1" type="field" hidden="0"/>
      <column name="METODE_3D" width="-1" type="field" hidden="0"/>
      <column name="MAALESTED" width="-1" type="field" hidden="0"/>
      <column name="UNDER_MIN" width="-1" type="field" hidden="0"/>
      <column name="TIMEOF_CRE" width="-1" type="field" hidden="0"/>
      <column name="TIMEOF_PUB" width="-1" type="field" hidden="0"/>
      <column name="TIMEOF_REV" width="-1" type="field" hidden="0"/>
      <column name="TIMEOF_EXP" width="-1" type="field" hidden="0"/>
      <column width="-1" type="actions" hidden="1"/>
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
    <field name="BBRAKTION" editable="1"/>
    <field name="BYGN_TYPE" editable="1"/>
    <field name="BYGN_UUID" editable="1"/>
    <field name="FEATSTATUS" editable="1"/>
    <field name="FEAT_KODE" editable="1"/>
    <field name="FEAT_TYPE" editable="1"/>
    <field name="FOT_ID" editable="1"/>
    <field name="GEOMSTATUS" editable="1"/>
    <field name="MAALESTED" editable="1"/>
    <field name="METODE_3D" editable="1"/>
    <field name="MOB_ID" editable="1"/>
    <field name="TIMEOF_CRE" editable="1"/>
    <field name="TIMEOF_EXP" editable="1"/>
    <field name="TIMEOF_PUB" editable="1"/>
    <field name="TIMEOF_REV" editable="1"/>
    <field name="UNDER_MIN" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="BBRAKTION" labelOnTop="0"/>
    <field name="BYGN_TYPE" labelOnTop="0"/>
    <field name="BYGN_UUID" labelOnTop="0"/>
    <field name="FEATSTATUS" labelOnTop="0"/>
    <field name="FEAT_KODE" labelOnTop="0"/>
    <field name="FEAT_TYPE" labelOnTop="0"/>
    <field name="FOT_ID" labelOnTop="0"/>
    <field name="GEOMSTATUS" labelOnTop="0"/>
    <field name="MAALESTED" labelOnTop="0"/>
    <field name="METODE_3D" labelOnTop="0"/>
    <field name="MOB_ID" labelOnTop="0"/>
    <field name="TIMEOF_CRE" labelOnTop="0"/>
    <field name="TIMEOF_EXP" labelOnTop="0"/>
    <field name="TIMEOF_PUB" labelOnTop="0"/>
    <field name="TIMEOF_REV" labelOnTop="0"/>
    <field name="UNDER_MIN" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>FOT_ID</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
