from __future__ import annotations

import matplotlib.pyplot as plt
import streamlit as st

try:
    from ..utils.shiftLogic import ShiftAnalysis
except ImportError:
    from utils.shiftLogic import ShiftAnalysis


def render_complexity_panel(analysis: ShiftAnalysis) -> None:
    st.subheader("Complexity Analysis Panel")

    m1, m2, m3 = st.columns(3)
    m1.metric("Row Shift (q mod sqrt(p))", analysis.row_shift)
    m2.metric("Column Shift (floor(q / sqrt(p)))", analysis.col_shift)
    m3.metric("Total Mesh Steps", analysis.mesh_steps)

    st.write(
        "Ring steps formula: min{q, p-q}  |  "
        "Mesh steps formula: (q mod sqrt(p)) + floor(q / sqrt(p))"
    )

    chart_col, text_col = st.columns([1, 1])

    with chart_col:
        fig, ax = plt.subplots(figsize=(4.5, 3))
        labels = ["Ring", "Mesh"]
        values = [analysis.ring_steps, analysis.mesh_steps]
        bars = ax.bar(labels, values, color=["#e07a5f", "#3d405b"])
        ax.set_ylabel("Step Count")
        ax.set_title("Communication Steps Comparison")
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h + 0.1, f"{int(h)}", ha="center", va="bottom")
        st.pyplot(fig)

    with text_col:
        if analysis.mesh_steps < analysis.ring_steps:
            st.success("Mesh is more efficient for this input.")
        elif analysis.mesh_steps == analysis.ring_steps:
            st.info("Mesh and Ring are equal for this input.")
        else:
            st.warning("Ring is more efficient for this input.")

        st.write(f"Ring steps: {analysis.ring_steps}")
        st.write(f"Mesh steps: {analysis.mesh_steps}")
        if analysis.ring_steps > 0:
            gain = (analysis.ring_steps - analysis.mesh_steps) / analysis.ring_steps * 100
            st.write(f"Relative improvement: {gain:.2f}%")
