import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

masterMaterialStacked = AssetTools.create_asset("M_Master_Stacked","/Game/masterMaterials", unreal.Material, unreal.MaterialFactoryNew())

#Create 2D Texture Param and Connect to Base Color

baseColorTextureParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked,unreal.MaterialExpressionTextureSampleParameter,-384,-200)
baseColorTextureParam.set_editor_property("Parameter_Name","Color")
MaterialEditLibrary.connect_material_property(baseColorTextureParam,"RGB",unreal.MaterialProperty.MP_BASE_COLOR)

#Create Constant Value and Connect to Specular
specParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked, unreal.MaterialExpressionConstant,-384,50)
specParam.set_editor_property("R",0.3)
MaterialEditLibrary.connect_material_property(specParam, "", unreal.MaterialProperty.MP_SPECULAR)

#Create 2D Texture Param and Connect to Normal
normalTextureParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked,unreal.MaterialExpressionTextureSampleParameter,-384,150)
normalTextureParam.set_editor_property("Parameter_Name","Normal")
MaterialEditLibrary.connect_material_property(normalTextureParam,"RGB",unreal.MaterialProperty.MP_NORMAL)

#Create 2D Texture Param and Connect to Ambient Occlusion
ormTextureParam = MaterialEditLibrary.create_material_expression(masterMaterialStacked,unreal.MaterialExpressionTextureSampleParameter,-384,350)
ormTextureParam.set_editor_property("Parameter_Name","ORM")
MaterialEditLibrary.connect_material_property(ormTextureParam,"R",unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
MaterialEditLibrary.connect_material_property(ormTextureParam,"G", unreal.MaterialProperty.MP_ROUGHNESS)
MaterialEditLibrary.connect_material_property(ormTextureParam,"B", unreal.MaterialProperty.MP_METALLIC)

#Create Material Instance
stackedMatInstance = AssetTools.create_asset("masterMatStacked_ORM_Inst", "/Game/MasterMaterials", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
stackedMatInstance.set_editor_property("Parent",masterMaterialStacked)

EditorAssetLibrary.save_asset("/Game/masterMaterials/M_Master_Stacked", True)
EditorAssetLibrary.save_asset("/Game/masterMaterials/masterMatStacked_ORM_Inst", True)