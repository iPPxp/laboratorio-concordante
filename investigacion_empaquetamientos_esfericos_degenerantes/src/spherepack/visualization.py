"""Exportador SVG minimo: produce una proyeccion, no una prueba tridimensional."""

from __future__ import annotations

from html import escape
import json
from pathlib import Path

import numpy as np

from .geometry import normalize_rows


def _project(points: np.ndarray) -> np.ndarray:
    # Proyeccion ortografica fija: permite inspeccion reproducible, no perspectiva.
    matrix = np.asarray(((0.8660254, -0.5, 0.0), (0.2886751, 0.5, -0.8164966)))
    return normalize_rows(points) @ matrix.T


def write_shell_svg(path: Path, title: str, points: np.ndarray) -> None:
    projection = _project(points)
    scale = 180.0
    width = height = 460
    circles = []
    for index, (x, y) in enumerate(projection):
        cx, cy = 230 + scale * x, 230 - scale * y
        circles.append(f'<circle cx="{cx:.3f}" cy="{cy:.3f}" r="7" fill="#1565c0"/><text x="{cx+10:.3f}" y="{cy-8:.3f}" font-size="12">{index}</text>')
    body = "\n  ".join(circles)
    path.write_text(
        f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="white"/>
  <line x1="30" y1="230" x2="430" y2="230" stroke="#b0bec5"/>
  <line x1="230" y1="30" x2="230" y2="430" stroke="#b0bec5"/>
  <text x="20" y="28" font-size="16" font-family="sans-serif">{escape(title)}</text>
  <text x="20" y="448" font-size="11" font-family="sans-serif">OBSERVACION_VISUAL: proyeccion ortografica fija; no sustituye la configuracion 3D.</text>
  {body}
</svg>\n''', encoding="utf-8", newline="\n"
    )


def write_interactive_html(path: Path, title: str, point_sets: dict[str, np.ndarray]) -> None:
    """Escribe un visor 3D local sin red ni bibliotecas de terceros.

    El archivo es una herramienta de inspeccion: su rotacion no calcula rigidez,
    contacto ni optimalidad. Esos valores proceden del modelo geometrico aparte.
    """
    serializable = {name: normalize_rows(points).round(12).tolist() for name, points in point_sets.items()}
    payload = json.dumps(serializable, ensure_ascii=False)
    path.write_text(
        f'''<!doctype html>
<html lang="es"><meta charset="utf-8"><title>{escape(title)}</title>
<style>body{{font-family:system-ui;margin:1rem}} canvas{{border:1px solid #90a4ae}} label{{margin-right:1rem}}</style>
<h1>{escape(title)}</h1>
<p><strong>OBSERVACION_VISUAL.</strong> Visor local de direcciones unitarias; no demuestra rigidez ni optimalidad.</p>
<label>Configuración <select id="set"></select></label><label>Rotación X <input id="rx" type="range" min="-180" max="180" value="18"></label><label>Rotación Y <input id="ry" type="range" min="-180" max="180" value="-28"></label>
<canvas id="view" width="720" height="560"></canvas>
<script>
const sets={payload}; const canvas=document.querySelector('#view'), ctx=canvas.getContext('2d');
const select=document.querySelector('#set'); Object.keys(sets).forEach(k=>select.add(new Option(k,k)));
function draw(){{const rx=+document.querySelector('#rx').value*Math.PI/180, ry=+document.querySelector('#ry').value*Math.PI/180;
 const cx=Math.cos(rx),sx=Math.sin(rx),cy=Math.cos(ry),sy=Math.sin(ry); const pts=sets[select.value].map((p,i)=>{{let [x,y,z]=p; let x1=cy*x+sy*z,z1=-sy*x+cy*z; let y1=cx*y-sx*z1,z2=sx*y+cx*z1; return {{i,x:x1,y:y1,z:z2}}}}).sort((a,b)=>a.z-b.z);
 ctx.clearRect(0,0,720,560);ctx.fillStyle='#fafafa';ctx.fillRect(0,0,720,560);ctx.strokeStyle='#b0bec5';ctx.beginPath();ctx.arc(360,280,210,0,Math.PI*2);ctx.stroke();
 ctx.fillStyle='#455a64';ctx.fillText('Proyección 3D local — '+select.value,20,28);pts.forEach(p=>{{const r=6+2*(p.z+1);ctx.beginPath();ctx.fillStyle='#1565c0';ctx.arc(360+205*p.x,280-205*p.y,r,0,Math.PI*2);ctx.fill();ctx.fillStyle='#111';ctx.fillText(String(p.i),368+205*p.x,274-205*p.y)}})}}
[select,document.querySelector('#rx'),document.querySelector('#ry')].forEach(e=>e.addEventListener('input',draw));draw();
</script></html>\n''', encoding="utf-8", newline="\n"
    )
