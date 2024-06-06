import i18n

import streamlit as st

from utils.init import init_once

i18n.set('load_path', ['locales']) # 번역 파일이 있는 디렉토리 경로
i18n.set('locale', 'en')  
i18n.set('fallback', 'en')  # 기본 언어가 없을 경우 사용할 언어 설정
i18n.set('file_format', 'json')

if __name__ == '__main__':
    # Init
    init_once()

    # Show title
    st.title(i18n.t('common.title'))

    # Show page description
    st.write(i18n.t('common.description'))

    # Show github link
    st.write(f'* Github: {i18n.t('common.github')}')
