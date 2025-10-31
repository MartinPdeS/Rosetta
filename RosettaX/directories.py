#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import RosettaX

__all__ = ["root_path", "doc_path", "logo_path", "doc_css_path"]

root_path = Path(RosettaX.__path__[0])

project_path = root_path.parents[0]

doc_path = root_path.parents[0].joinpath("docs")

logo_path = doc_path.joinpath("images/logo.png")

doc_css_path = doc_path.joinpath("source/_static/default.css")

if __name__ == "__main__":
    for path_name in __all__:
        path = locals()[path_name]
        print(path)
        assert path.exists(), f"Path {path_name} do not exists"

# -
