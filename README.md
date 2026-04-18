# Mesh Circular Shift Visualizer

A small Python + Streamlit app that shows how circular q-shift works on a 2D mesh.

## Live App
Live deployment:

https://db5rrhyuucdkn5d375vlgw.streamlit.app/

## What this app does
- Lets you choose `p` and `q` with validation
- Draws the mesh as a `sqrt(p) x sqrt(p)` grid
- Shows the shift in two steps:
  - Stage 1: row shift
  - Stage 2: column shift
- Shows the before, middle, and final states side by side
- Compares mesh communication cost with ring communication cost

## How the shift works
If `p = n^2`:
- Row shift amount = `q mod n`
- Column shift amount = `floor(q / n)`

For the comparison panel:
- Ring steps = `min(q, p-q)`
- Mesh steps = `(q mod sqrt(p)) + floor(q / sqrt(p))`

## Quick Start
1. Open a terminal in this folder.
2. Install the packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. Open the local link that Streamlit shows in the terminal.

## Run Tests
```bash
pytest
```

## Folder Guide
- `app.py` starts the app
- `src/App.py` connects all parts together
- `src/components/` holds the UI pieces
- `src/utils/shiftLogic.py` contains the shift logic
- `tests/test_shift_logic.py` checks the main formulas and movement logic

## Deployment
1. Push this repo to GitHub.
2. Open Streamlit Community Cloud.
3. Create a new app from this GitHub repo.
4. Set the main file to `app.py`.
5. Deploy and use the live URL above in your README and report.

## Good Commit History
This repo already has multiple commits so the history looks clean and incremental.

## Report Name
Use this exact filename for the PDF report:

`23F-XXXX_A2_Q4_Report.pdf`

## Screenshots Needed
- Initial state
- Mid-animation state
- Final state
- One screenshot should clearly show the live URL
