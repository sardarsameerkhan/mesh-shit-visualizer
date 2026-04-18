from __future__ import annotations

from math import isqrt

import streamlit as st

try:
    from ..utils.shiftLogic import is_perfect_square, validate_inputs
except ImportError:
    from utils.shiftLogic import is_perfect_square, validate_inputs


def render_control_panel(default_p: int = 16, default_q: int = 5) -> tuple[int, int, bool]:
    st.sidebar.header("Input Controls")
    p = st.sidebar.number_input("p (4-64, perfect square)", min_value=4, max_value=64, value=default_p, step=1)
    max_q = max(1, int(p) - 1)
    q = st.sidebar.number_input("q (1 to p-1)", min_value=1, max_value=max_q, value=min(default_q, max_q), step=1)

    if not is_perfect_square(int(p)):
        st.sidebar.error(f"p={int(p)} is not a perfect square. Closest valid values include {isqrt(int(p)) ** 2} and {(isqrt(int(p)) + 1) ** 2}.")

    is_valid, message = validate_inputs(int(p), int(q))
    if not is_valid:
        st.sidebar.warning(message)
    else:
        st.sidebar.success("Inputs are valid.")

    animate = st.sidebar.button("Run Stage-by-Stage Animation", use_container_width=True)
    st.sidebar.caption("Animation shows: Before -> Stage 1 (row shift) -> Stage 2 (column shift)")

    return int(p), int(q), is_valid and animate
