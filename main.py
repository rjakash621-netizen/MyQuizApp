import tkinter as _tk
from tkinter import messagebox as _mb
import json as _j
import os as _o
import base64 as _b

# Data ko encode kar diya gaya hai taaki answers na dikhein
_d_str = "W3sicSI6ICJDYXBpdGFsIG9mIFB1cnRnYWw/IiwgIm8iOiBbIk9zbG8iLCAiQnVkYXBvc3QiLCAibGlzYmFuIiwgIm90YXZhIl0sICJhIjogImxpc2JhbiJ9LCB7InEiOiAiaG93IG1hbnkgY29udGluZW50IGluIHdvcmxkPyIsICJvIjogWyIyIiwgIjciLCAiNCIsICI2Il0sICJhIjogIjcifSwgeyJxIjogIkhxIG9mIHdobz8iLCAibyI6IFsibmV3eW9yayIsICJqZW5ldmEiLCAibWFkcmlkIiwgInJvbWUiXSwgImEiOiAiamVuZXZhIn0sIHsicSI6ICJjYXBpdGFsIG9mIHJ1c3NpYT8iLCAibyI6IFsibWFzY28iLCAic2l5b2wiLCAiYmFybGluIiwgImtlcHRvd24iXSwgImEiOiAibWFzY28ifSwgeyJxIjogImN1cnJlbmN5IG9mIHVzYT8iLCAibyI6IFsiRXVybyIsICJkb2xsYXIiLCAicnViYWwiLCAia3lhdCJdLCAiYSI6ICJkb2xsYXIifV0="
_qz = _j.loads(_b.b64decode(_d_str).decode())

class _App:
    def __init__(self, _r):
        self._r = _r
        self._i = 0
        self._u = [None] * len(_qz)
        self._s = True
        self._r.bind("<FocusOut>", self._f_o)
        self._l = _tk.Label(_r, text="", font=("Arial", 12))
        self._l.pack(pady=20)
        self._v = _tk.StringVar()
        self._rb = []
        for _ in range(4):
            _b_obj = _tk.Radiobutton(_r, text="", variable=self._v, value="", font=("Arial", 10))
            _b_obj.pack(anchor="w", padx=20)
            self._rb.append(_b_obj)
        _tk.Button(_r, text="Back", command=self._bk).pack(pady=5)
        self._nx_b = _tk.Button(_r, text="Next", command=self._nx)
        self._nx_b.pack(pady=5)
        self._ld()

    def _ld(self):
        _curr = _qz[self._i]
        self._l.config(text=_curr["q"])
        for _x in range(4):
            self._rb[_x].config(text=_curr["o"][_x], value=_curr["o"][_x])
        self._v.set(self._u[self._i] if self._u[self._i] else "")
        self._nx_b.config(text="Submit" if self._i == len(_qz) - 1 else "Next")

    def _bk(self):
        if self._i > 0:
            self._u[self._i] = self._v.get()
            self._i -= 1
            self._ld()

    def _nx(self):
        self._u[self._i] = self._v.get()
        if self._i < len(_qz) - 1:
            self._i += 1
            self._ld()
        else: self._fin()

    def _f_o(self, _e):
        if self._s: self._fin()

    def _fin(self):
        if not self._s: return
        self._s = False
        _sc = sum(1 for _k, _v in enumerate(self._u) if _v == _qz[_k]["a"])
        with open("status.json", "w") as _f:
            _j.dump({"s": True, "r": _sc}, _f)
        _mb.showinfo("Done", f"Score: {_sc}/{len(_qz)}")
        self._r.destroy()

if _o.path.exists("status.json"): exit()
_root = _tk.Tk()
_root.geometry("300x400")
_App(_root)
_root.mainloop()
