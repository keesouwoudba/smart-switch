---
name: Block-Logic Director
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#ebbbb4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#b18780'
  outline-variant: '#603e39'
  surface-tint: '#ffb4a8'
  primary: '#ffb4a8'
  on-primary: '#690100'
  primary-container: '#ff5540'
  on-primary-container: '#5c0000'
  inverse-primary: '#c00100'
  secondary: '#66dd8b'
  on-secondary: '#003919'
  secondary-container: '#25a55a'
  on-secondary-container: '#003115'
  tertiary: '#c7c6c6'
  on-tertiary: '#2f3031'
  tertiary-container: '#919191'
  on-tertiary-container: '#292a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930100'
  secondary-fixed: '#83fba5'
  secondary-fixed-dim: '#66dd8b'
  on-secondary-fixed: '#00210c'
  on-secondary-fixed-variant: '#005227'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c7c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  body-reg:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-pixel:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
spacing:
  block-unit: 4px
  gutter: 16px
  container-padding: 24px
  viewport-margin: 32px
---

## Brand & Style

This design system is a **Tactile Retro-Pixel** interface tailored for high-fidelity circuit simulation. It merges the nostalgic aesthetic of 8-bit voxel gaming with the functional requirements of a technical dashboard. The brand personality is industrious, technical, and immersive, evoking the feeling of operating a complex machine within a digital workshop.

The visual style leans heavily into **Skeuomorphic Pixel Art**. Every element is treated as a physical "block" or "plate" within a 3D grid. The target audience includes engineers, hobbyists, and gamers who value tactile feedback and high-contrast logic visualization. The emotional response is one of focus and "tinkering," where every click feels substantial and every active state feels powered by a tangible energy source.

## Colors

The palette is rooted in the "Underground" aesthetic of the source inspiration. **Obsidian-black** serves as the primary canvas color, providing a high-contrast backdrop that makes active logic pop. 

- **Redstone-red** is reserved exclusively for active states, high-voltage signals, and "On" logic.
- **Emerald-green** functions as a utility accent for success states, power-saving modes, and finalized connections.
- **Stone-gray** acts as the structural foundation, used for borders, inactive containers, and "unpowered" paths.
- **Deep Slate** (Neutral) is used for secondary backgrounds to create a sense of depth and layering between different panels of the dashboard.

## Typography

While **Space Grotesk** is utilized as the technical base font for its geometric and "tech" appearance, it must be rendered using a specific **pixel-aliasing CSS filter** or a fallback "Minecraftia" webfont to achieve the desired 8-bit aesthetic. 

Headers and labels should always appear in "Pixel-Art" style with no anti-aliasing. Labels should be small and uppercase to mimic the classic inventory tooltips. For technical readouts where legibility is paramount (like numerical data), the font should maintain its blocky weight but remain high-contrast against the Obsidian backgrounds.

## Layout & Spacing

The layout follows a **Fixed-Block Grid**. Every component's width and height must be a multiple of the 4px "block-unit." This ensures that pixel-art borders align perfectly without sub-pixel blurring.

The dashboard uses a structured, multi-panel approach:
1.  **Primary Viewport:** A central "Stone Brick" bordered window for the circuit simulation.
2.  **Sidebars:** Fixed-width 280px panels for component libraries and logic properties.
3.  **Toolbar:** A "Hotbar" style bottom-docked menu for quick-access tools.

Gaps between panels should be 16px, representing a "clear block" of space, maintaining the rigid, grid-locked feel of the environment.

## Elevation & Depth

Depth is conveyed through **Physical Extrusion** rather than soft shadows. This design system uses "Inset" and "Outset" border techniques:
- **Level 0 (Background):** Flat Obsidian-black.
- **Level 1 (Panels):** Stone-gray borders with a 4px "shadow" border on the bottom and right edges to simulate a raised block.
- **Level 2 (Buttons/Interactive):** 3D-extruded plates. When hovered, the bottom shadow thickness decreases; when pressed, the element shifts 2px down and right to simulate physical depression.

No blur or transparency is permitted; depth must be represented by solid-color pixel offsets and geometric shading.

## Shapes

The design system strictly adheres to a **Sharp (0)** roundedness policy. In this world, there are no curves. All "circular" elements (like logic gates or ports) must be constructed from stepped pixels to approximate a circle while maintaining a 0px border radius. All container corners are 90-degree angles.

## Components

### Buttons (Pressure Plates)
- **Wooden Plate (Primary):** Light brown texture with dark brown 4px bottom border. Used for "Start" or "Execute" actions.
- **Stone Plate (Secondary):** Light gray texture with Stone-gray 4px bottom border. Used for "Stop" or "Reset" actions.

### Toggle Switches (Redstone Lamps)
- **Off State:** Dark brown/black checkered texture with a faint Stone-gray frame.
- **On State:** Bright Orange/Red glowing texture with a "Bloom" effect achieved by a solid Redstone-red outer 1px border.

### Viewport (The Stone Brick Container)
The primary video viewport must feature a repeating "Stone Brick" texture border. This border should be 8px thick, consisting of light-gray highlights and dark-gray mortar lines, framing the high-fidelity circuit simulation.

### Logic Chips
Small, flat Stone-gray rectangles with 1px black inner borders. Inputs and outputs are represented by 4x4 pixel squares that turn Redstone-red when a signal is high.

### Checkboxes
Styled as small "Lever" icons. When checked, the lever handle is angled down; when unchecked, it is angled up.

### Input Fields
Styled as "Sign" boards. A light oak-colored background with dark-brown pixelated text, featuring a 2px dark-brown border.