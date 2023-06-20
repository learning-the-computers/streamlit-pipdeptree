import subprocess
import sys

import streamlit as st

installed_packages = sorted({package.decode() for package in subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).splitlines()}, key=str.lower)

multi_select_packages = st.multiselect('Select packages', installed_packages)
