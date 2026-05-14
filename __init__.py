# MIT License
# Copyright (c) 2023 Thomas 'noio' van den Berg
# Blender 5 port by community — auto_load.py fix for extension package naming

import bpy
import traceback

try:
    from . import auto_load
    print(f"[PixelUnwrap] __package__ = {__package__}")
    auto_load.init(__package__)
    print(f"[PixelUnwrap] auto_load.init() succeeded")
except Exception as e:
    print(f"[PixelUnwrap] ERROR during init: {e}")
    traceback.print_exc()


def register():
    auto_load.register()

    bpy.types.Scene.pixunwrap_texel_density = bpy.props.FloatProperty(
        name="Pixels Per Unit",
        default=16,
        description="",
    )
    bpy.types.Scene.pixunwrap_default_texture_size = bpy.props.IntProperty(
        name="Default Texture Size",
        default=64,
        description="This is also used when unwrapping objects that have no texture assigned",
    )
    bpy.types.Scene.pixunwrap_texture_fill_color_tl = bpy.props.FloatVectorProperty(
        name="Texture Fill A",
        default=[0.92, 0.69, 0.69],
        description="Color used to fill top left quadrant of empty texture",
        subtype="COLOR",
        min=0,
        max=1,
    )
    bpy.types.Scene.pixunwrap_texture_fill_color_bl = bpy.props.FloatVectorProperty(
        name="Texture Fill B",
        default=[0.72, 0.72, 0.84],
        description="Color used to fill bottom left quadrant of empty texture",
        subtype="COLOR",
        min=0,
        max=1,
    )
    bpy.types.Scene.pixunwrap_texture_fill_color_tr = bpy.props.FloatVectorProperty(
        name="Texture Fill C",
        default=[0.64, 0.91, 0.64],
        description="Color used to fill top right quadrant of empty texture",
        subtype="COLOR",
        min=0,
        max=1,
    )
    bpy.types.Scene.pixunwrap_texture_fill_color_br = bpy.props.FloatVectorProperty(
        name="Texture Fill D",
        default=[1, 0.79, 0.48],
        description="Color used to fill bottom right quadrant of empty texture",
        subtype="COLOR",
        min=0,
        max=1,
    )

    uv_behaviors = (
        ("DESTRUCTIVE", "Destructive", ""),
        ("PRESERVE", "Preserve Texture", ""),
    )
    bpy.types.Scene.pixunwrap_uv_behavior = bpy.props.EnumProperty(
        name="UV Change Behavior",
        default=0,
        description="When using UV operators, should the image be modified to preserve texturing",
        items=uv_behaviors,
    )
    bpy.types.Scene.pixunwrap_modify_texture = bpy.props.BoolProperty(
        name="Modify Texture",
        default=False,
        description="Should the texture be modified to keep painted pixels in place on the model, or can UV's be moved freely.",
    )
    bpy.types.Scene.pixunwrap_fold_sections = bpy.props.IntProperty(
        name="Fold Sections",
        default=2,
        description="How many sections to fold the selected UV grid into.",
    )
    bpy.types.Scene.pixunwrap_fold_alternate = bpy.props.BoolProperty(
        name="Fold Alternate",
        default=False,
        description="Alternate directions of folded sections in a zig-zag way. Turn off to cut and stack sections",
    )


def unregister():
    auto_load.unregister()
