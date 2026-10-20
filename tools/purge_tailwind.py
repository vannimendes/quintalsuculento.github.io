#!/usr/bin/env python3
"""
Gera um CSS enxuto a partir do Tailwind 2.2.19 completo.

Mantém somente:
  - regras base (elementos, ::before/::after, variáveis --tw-*), que não dependem de classes;
  - regras de classes que aparecem em algum dos arquivos HTML informados
    (inclusive classes citadas dentro de <script>), com suas variantes
    responsivas (sm:, md:, lg:...) e de estado (hover:, focus:, ...);
  - @keyframes somente quando alguma animação os usa.

A ordem original das regras é preservada, então a cascata não muda.

Uso:
  python3 tools/purge_tailwind.py caminho/para/tailwind.min.css index.html [outros.html] -o tailwind.purged.css

Como obter o tailwind.min.css completo (só é preciso para gerar de novo):
  https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css

Sempre que o HTML passar a usar uma classe nova do Tailwind, rode este script de novo.
"""
import argparse
import pathlib
import re
import sys


def strip_comments(css):
    return re.sub(r'/\*.*?\*/', '', css, flags=re.S)


def parse(css):
    """Divide em blocos de nível superior: (prelude, corpo)."""
    out, i, n = [], 0, len(css)
    while i < n:
        while i < n and css[i] in ' \t\r\n':
            i += 1
        if i >= n:
            break
        j = i
        while j < n and css[j] not in '{;':
            j += 1
        if j >= n:
            break
        if css[j] == ';':                      # at-rule sem corpo (@charset, @import)
            out.append((css[i:j].strip(), None))
            i = j + 1
            continue
        depth, k = 1, j + 1
        while k < n and depth:
            c = css[k]
            if c in '"\'':                      # pula strings
                q = c
                k += 1
                while k < n and css[k] != q:
                    k += 2 if css[k] == '\\' else 1
            elif c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
            k += 1
        out.append((css[i:j].strip(), css[j + 1:k - 1]))
        i = k
    return out


def split_selectors(sel):
    parts, depth, cur, q = [], 0, [], None
    for c in sel:
        if q:
            cur.append(c)
            if c == q:
                q = None
            continue
        if c in '"\'':
            q = c
        elif c in '([':
            depth += 1
        elif c in ')]':
            depth -= 1
        if c == ',' and depth == 0:
            parts.append(''.join(cur).strip())
            cur = []
        else:
            cur.append(c)
    parts.append(''.join(cur).strip())
    return [p for p in parts if p]


CLASS_RE = re.compile(r'\.((?:\\.|[A-Za-z0-9_-])+)')


def unescape(name):
    name = re.sub(r'\\([0-9a-fA-F]{1,6}) ?', lambda m: chr(int(m.group(1), 16)), name)
    return re.sub(r'\\(.)', r'\1', name)


def classes_in(selector):
    # ignora o que está dentro de colchetes de atributo
    no_attr = re.sub(r'\[[^\]]*\]', '', selector)
    return [unescape(m) for m in CLASS_RE.findall(no_attr)]


def filter_rules(css, used, keyframes):
    out = []
    for prelude, body in parse(css):
        if body is None:
            out.append(prelude + ';')
        elif prelude.startswith(('@media', '@supports')):
            inner = filter_rules(body, used, keyframes)
            if inner:
                out.append(f'{prelude}{{{inner}}}')
        elif 'keyframes' in prelude.split('{')[0] and prelude.startswith('@'):
            keyframes.append((prelude, body))
        elif prelude.startswith('@'):
            out.append(f'{prelude}{{{body}}}')
        else:
            kept = [s for s in split_selectors(prelude)
                    if all(c in used for c in classes_in(s))]
            if kept:
                out.append(f'{",".join(kept)}{{{body}}}')
    return ''.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tailwind')
    ap.add_argument('html', nargs='+')
    ap.add_argument('-o', '--output', required=True)
    a = ap.parse_args()

    text = ' '.join(pathlib.Path(h).read_text(encoding='utf8') for h in a.html)
    used = set(re.findall(r'[^\s"\'`<>=(){};,]+', text))

    full = strip_comments(pathlib.Path(a.tailwind).read_text(encoding='utf8'))
    keyframes = []
    css = filter_rules(full, used, keyframes)
    for prelude, body in keyframes:
        name = prelude.split()[-1]
        if re.search(r'animation[^;{}]*\b' + re.escape(name) + r'\b', css):
            css += f'{prelude}{{{body}}}'

    header = '/*! Tailwind CSS v2.2.19 (MIT) - versão enxuta gerada por tools/purge_tailwind.py */\n'
    pathlib.Path(a.output).write_text(header + css + '\n', encoding='utf8')
    print(f'{len(full)/1024:.0f} KB -> {len(css)/1024:.1f} KB ({100*len(css)/len(full):.2f}%)', file=sys.stderr)


if __name__ == '__main__':
    main()
