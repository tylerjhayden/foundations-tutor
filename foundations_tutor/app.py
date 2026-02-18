"""Streamlit multi-page app."""
import streamlit as st
from foundations_tutor.pages import catalog, lesson, progress, settings


def main() -> None:
    st.set_page_config(page_title="Foundations Tutor", page_icon="📚", layout="wide")
    pg = st.navigation([
        st.Page(catalog.page, title="Catalog", icon="📚"),
        st.Page(lesson.page,  title="Lesson",  icon="💬"),
        st.Page(progress.page, title="Progress", icon="📊"),
        st.Page(settings.page, title="Settings", icon="⚙️"),
    ])
    pg.run()
