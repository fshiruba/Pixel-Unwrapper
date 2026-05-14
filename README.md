> **WARNING: EARLY ALPHA VERSION.**
> **CAN CRASH BLENDER.**
> **USE AT YOUR OWN RISK AND SAVE REGULARLY**

# Pixel Perfect Unwrapping for Blender

This is an add-on for Blender that helps creating **Pixel Art 3D** or **lo-fi 3D**. This style looks best when:

1. Pixels align with edges on models
2. Pixels are roughly the same size across the model

Blender's standard unwrapping tools can make this tedious. This add-on makes that easier.

[![Walkthrough on YouTube](https://user-images.githubusercontent.com/271730/224333278-0fdfa82c-cd5d-4601-a2b8-563e29f4f493.png)](https://youtu.be/9ao1PM7GTS8)

---

## Blender 5 Compatibility Fork

This is a community fork of the original [Pixel-Unwrapper by Thomas 'noio' van den Berg](https://github.com/noio/Pixel-Unwrapper), updated to work with **Blender 5.0+**.

### What changed

The original addon used the legacy `bl_info` registration system, which was removed in Blender 5. This fork replaces it with a `blender_manifest.toml` file as required by Blender's modern extension system. No functional code was changed — all operators, UV logic, and texture tools are identical to the original.

**Changes made:**
- Removed `bl_info` dict from `__init__.py`
- Added `blender_manifest.toml` for Blender 5+ extension registration
- Updated `README.md` with compatibility notes and updated installation instructions

If you find any bugs introduced by the Blender 5 API, please open an issue. If the original author updates the upstream repo, consider using that instead and opening a PR there.

---

## Installation (Blender 5+)

1. Go to [Releases](../../releases/latest) and download the **Source code (zip)**
2. In Blender, go to **Edit → Preferences → Add-ons**
3. Click the dropdown arrow next to the **Install** button and choose **Install from Disk...**
4. Select the downloaded `.zip` file

> **Note:** Blender 5 uses a new extension system. Do **not** use the old drag-and-drop or legacy Install button — use **Install from Disk** from the dropdown.

## Installation (Blender 4.2 – 4.x)

For Blender 4.x, use the [original repository](https://github.com/noio/Pixel-Unwrapper) instead — it targets `(4, 3, 0)` and installs via the classic Add-ons panel.

---

## Features

[![Texture Setup](https://github.com/noio/Pixel-Unwrapper/raw/main/docs/texture_setup.png)](https://github.com/noio/Pixel-Unwrapper/blob/main/docs/texture_setup.png)

### Pixels Per Unit

To make it easy to stick to a consistent pixel size across the model, you set your desired **Pixel Density** here. The [Unwrapping](#unwrapping) operators, as well as the [Rescale Selection](#rescale-selection) operator, use this to determine the UV scale.

Because most operators take into account Pixel Density and texture size, they will only work **if the active object has a texture**.

### Create Texture

If your model does not have a material with a texture yet, use this button to create them. It will also set the *Texture Interpolation* to *Closest*.

---

## Unwrapping

[![Unwrapping](https://github.com/noio/Pixel-Unwrapper/raw/main/docs/unwrapping.png)](https://github.com/noio/Pixel-Unwrapper/blob/main/docs/unwrapping.png)

### Unwrap Basic

[![Unwrap Basic](https://github.com/noio/Pixel-Unwrapper/raw/main/docs/unwrap_basic.png)](https://github.com/noio/Pixel-Unwrapper/blob/main/docs/unwrap_basic.png)

Performs a standard Blender Unwrap operation, but scales the result to match the Pixel Density. Then, it will scale and move the selection so that **the bounds align with pixel edges on the texture**. Internal vertices are not snapped to pixels.

### Unwrap Grid

[![Unwrap Grid](https://github.com/noio/Pixel-Unwrapper/raw/main/docs/unwrap_grid.png)](https://github.com/noio/Pixel-Unwrapper/blob/main/docs/unwrap_grid.png)

Detects a **grid of quads** in the selection and maps each **row and column** to the closest multiple of whole pixels (applying the Pixel Density). Any attached non-quads are unwrapped using Blender's standard unwrap. If the quads in your model are very deformed, the pixels will be distorted too.

### Unwrap to Single Pixel

[![Unwrap to Single Pixel](https://github.com/noio/Pixel-Unwrapper/raw/main/docs/unwrap_to_single_pixel.png)](https://github.com/noio/Pixel-Unwrapper/blob/main/docs/unwrap_to_single_pixel.png)

Maps selected faces to a single pixel on the texture. Each application maps the selection to a free bit of texture so you can fill it with a different color. Useful for faces you just want as a flat color.

---

## UV Editing

[![UV Editing](https://github.com/noio/Pixel-Unwrapper/raw/main/docs/uv_editing.png)](https://github.com/noio/Pixel-Unwrapper/blob/main/docs/uv_editing.png)

Some UV operators can be applied **while preserving the bits of texture you have already painted**.

- **Destructive** mode is the normal mode. UV faces move freely; any painted texture becomes jumbled.
- **Preserve Texture** will attempt to **move pixels on the texture** as the operator is applied, preserving how the texture fits on the model.

### Flip
Flips the selected faces on the UV map using pixel-snapped UV bounds.

### Rotate
Rotates the selected faces 90 degrees CCW on the UV map. In **Preserve Texture** mode, the island is moved to free UV space first so the original texture can be copied without overwriting other islands.

### Rescale Selection
Rescales the selection to match the Pixel Density.

### Selection to Free Space
Moves the selection to a free bit of UV space. In **Preserve Texture** mode, it copies the texture pixels to the new UV location.

The plugin assumes that **texture size is not an issue**. Pixel art textures are so small that efficient texture space usage is not a priority. This lets you start texture painting before finalizing UV mapping — there's always space to paint newly added geometry later. If you're worried about GPU memory for game assets, use a packing tool as a final step. The original author recommended [SpriteUV](https://www.spriteuv.com).

### Randomize Islands

[![Randomize Islands](https://github.com/noio/Pixel-Unwrapper/raw/main/docs/randomize_islands.png)](https://github.com/noio/Pixel-Unwrapper/blob/main/docs/randomize_islands.png)

Moves each island to a random position on the UV map. Useful for assigning random sections of a uniform texture (tree bark, ground dirt, etc).

### Repack All
Repacks all islands onto the bottom of the UV map, freeing up texture space. Islands will be rotated for a tighter fit **unless** they were manually rotated using the [Rotate](#rotate) operator.

---

## Caveats

- Not all operators handle a single texture used on multiple objects. For example, [Repack All](#repack-all) will not account for faces on other objects when packing.
- The plugin does not distinguish between multiple materials on the same object. It treats all faces as if they use the same texture when deciding what is "free UV space".

---

## Credits

Original addon by **Thomas 'noio' van den Berg** — [github.com/noio](https://github.com/noio)

All credit for the design, implementation, and core logic goes to the original author. This fork only adds the `blender_manifest.toml` required for Blender 5+ compatibility. The original source is MIT licensed; this fork is distributed under the same terms.

If the original repository is updated with Blender 5 support, please use that instead: [github.com/noio/Pixel-Unwrapper](https://github.com/noio/Pixel-Unwrapper)

---

## License

MIT License — see [LICENSE](LICENSE) for full text.
