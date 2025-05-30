# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['mainG3.py'],
    pathex=[],
    binaries=[],
    datas=[('background.png', '.'), ('background2.png', '.'), ('ballista1.png', '.'), ('ballista2.png', '.'), ('heart.png', '.'), ('death.png', '.'), ('shot.mp3', '.'), ('hit.mp3', '.'), ('win.mp3', '.'), ('theme.json', '.'), ('bg1.mp3', '.'), ('bg2.mp3', '.'), ('logo.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='mainG3',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
