import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

masterMaterial = AssetTools.create_asset("M_Master","/Game/MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

#Create 2D Texture Param and Connect to Base Color

baseColorTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial,unreal.MaterialExpressionTextureSampleParameter,-384,-200)
baseColorTextureParam.set_editor_property("Parameter_Name","Color")
MaterialEditLibrary.connect_material_property(baseColorTextureParam,"RGB",unreal.MaterialProperty.MP_BASE_COLOR)

#Create 2D Texture Param and Connect to Base Color
roughnessTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial,unreal.MaterialExpressionTextureSampleParameter,-384,0)
roughnessTextureParam.set_editor_property("Parameter_Name","Roughness")
MaterialEditLibrary.connect_material_property(roughnessTextureParam,"RGB",unreal.MaterialProperty.MP_ROUGHNESS)

#Create Constant Value and Connect to Specular
specParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionConstant,-384,250)
specParam.set_editor_property("R",0.3)
MaterialEditLibrary.connect_material_property(specParam, "", unreal.MaterialProperty.MP_SPECULAR)

#Create 2D Texture Param and Connect to Normal
normalTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial,unreal.MaterialExpressionTextureSampleParameter,-384,350)
normalTextureParam.set_editor_property("Parameter_Name","Normal")
MaterialEditLibrary.connect_material_property(normalTextureParam,"RGB",unreal.MaterialProperty.MP_NORMAL)

#Create 2D Texture Param and Connect to Metallic
metalTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial,unreal.MaterialExpressionTextureSampleParameter,-384,550)
metalTextureParam.set_editor_property("Parameter_Name","Metalness")
MaterialEditLibrary.connect_material_property(metalTextureParam,"RGB",unreal.MaterialProperty.MP_METALLIC)

#Create 2D Texture Param and Connect to Ambient Occlusion
aoTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial,unreal.MaterialExpressionTextureSampleParameter,-384,750)
aoTextureParam.set_editor_property("Parameter_Name","Ambient Occlusion")
MaterialEditLibrary.connect_material_property(aoTextureParam,"RGB",unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)

EditorAssetLibrary.save_asset("/Game/MasterMaterials/M_Master", True)