from __future__ import annotations

import streamlit as st

try:
    from .components.ComplexityPanel import render_complexity_panel
    from .components.ControlPanel import render_control_panel
    from .components.MeshGrid import render_before_after, run_animation
    from .utils.shiftLogic import analyze_complexity, apply_two_stage_mesh_shift
except ImportError:
    from components.ComplexityPanel import render_complexity_panel
    from components.ControlPanel import render_control_panel
    from components.MeshGrid import render_before_after, run_animation
    from utils.shiftLogic import analyze_complexity, apply_two_stage_mesh_shift


def run_app() -> None:
    st.set_page_config(page_title="Mesh Circular Shift Visualizer", page_icon="#", layout="wide")
    st.title("Mesh Circular Shift Visualizer")
    st.caption("Interactive simulation of circular q-shift on a 2D mesh topology")

    p, q, animate = render_control_panel(default_p=16, default_q=5)

    initial, after_row, after_col = apply_two_stage_mesh_shift(p, q)
    analysis = analyze_complexity(p, q)

    st.markdown("### Before/After States")
    render_before_after(initial, after_row, after_col)

    st.markdown("---")
    render_complexity_panel(analysis)

    st.markdown("---")
    st.markdown("### Stage-by-Stage Animation")
    if animate:
        run_animation(initial, after_row, after_col, analysis.row_shift, analysis.col_shift)
    else:
        st.info("Click 'Run Stage-by-Stage Animation' in the sidebar to animate.")
