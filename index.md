---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "handl-lang"
  text: "Arrows, not functions"
  tagline: "Language, programs, laws, coherence, and effects: all data."
  actions:
    - theme: brand
      text: Ecosystem
      link: /ecosystem/
    - theme: alt
      text: Kernel docs
      link: /kernel/

features:
  - title: Arrows, not functions
    details: "Computation composes as arrows: inspectable structure, not closures you can only call."
  - title: Serializable
    details: "Programs, laws, and effects are data: they round-trip through JSON, YAML, and any engine's memory model."
  - title: Globular
    details: "Programs are 1-morphisms, laws and rewrites are 2-morphisms, and transformations extend into higher dimensions."
  - title: Graded effects
    details: "Operations carry grades and handlers supply meaning: effects are algebraic and first-class."
  - title: Language as data
    details: "Syntax, grammar, AST shapes, eval schemes, and type rules are declarative, not hardcoded into engines."
  - title: Runtime-independent
    details: "One IR feeds tree-walk, bytecode, Cranelift, LLVM, Triton, and CUDA backends interchangeably."
---

<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  const hero = document.querySelector('.VPHero')
  if (!hero) return

  const canvas = document.createElement('canvas')
  canvas.style.position = 'absolute'
  canvas.style.inset = '0'
  canvas.style.width = '100%'
  canvas.style.height = '100%'
  canvas.style.fontSize = '12px'
  canvas.style.fontFamily = 'var(--vp-font-family-mono)'
  canvas.style.zIndex = '0'
  hero.style.position = 'relative'
  hero.insertBefore(canvas, hero.firstChild)

  const ctx = canvas.getContext('2d')

  const settings = {
    maxDepth: 4,
    lineHeight: 18,
    space: 6,
    alpha: 0.18
  }

  const pick = (arr) => arr[Math.floor(Math.random() * arr.length)]

  // The kernel vocabulary: the six closed combinators and the
  // object/arrow forms. This is the published calculus.
  const arrows = ['f', 'g', 'h', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w']
  const types = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'Obj', 'State', 'Input', 'Output', 'World'
  ]
  const grades = ['Op', 'Query', 'Command', 'Event', 'IO', 'Net', 'Time', 'Rand']
  const p = (s) => s

  const ty = () => pick(types)
  const arr = () => pick(arrows)

  function typeExpr(depth = 0) {
    if (depth >= settings.maxDepth) return [ty()]
    const roll = Math.random()
    if (roll < 0.30) return [ty()]
    if (roll < 0.50) return [ty(), p('~>'), ty()]
    if (roll < 0.65) return [p('('), ty(), p(','), ty(), p(')'), p('~>'), ty()]
    if (roll < 0.78) return [ty(), p('~['), pick(grades), p(']~>'), ty()]
    if (roll < 0.90) return [ty(), p('*'), ty()]
    return [ty(), p('+'), ty()]
  }

  function arrowExpr(depth = 0) {
    if (depth >= settings.maxDepth) return [arr()]
    const roll = Math.random()
    if (roll < 0.22) return [arr()]
    if (roll < 0.40) return [arr(), p('>>>'), ...arrowExpr(depth + 1)]
    if (roll < 0.52) return [arr(), p('&&&'), arr()]
    if (roll < 0.62) return [arr(), p('|||'), arr()]
    if (roll < 0.72) return [p('first'), p('('), ...arrowExpr(depth + 1), p(')')]
    if (roll < 0.80) return [p('loop'), p('('), ...arrowExpr(depth + 1), p(')')]
    if (roll < 0.88) return [p('arr'), p('('), ty(), p('->'), ty(), p(')')]
    if (roll < 0.94) return [p('app'), p('('), arr(), p(','), ty(), p(')')]
    return [p('('), ...arrowExpr(depth + 1), p(')')]
  }

  function stmt() {
    const roll = Math.random()
    if (roll < 0.35) return [arr(), p(':'), ...typeExpr(), p(';')]
    if (roll < 0.70) return [arr(), p('='), ...arrowExpr(), p(';')]
    if (roll < 0.85) return [p('sym'), p('('), ty(), p(')'), p(';')]
    return [...arrowExpr(), p('>>>'), ...arrowExpr(), p(';')]
  }

  function draw() {
    const rect = hero.getBoundingClientRect()
    const dpr = window.devicePixelRatio || 1
    canvas.width = Math.floor(rect.width * dpr)
    canvas.height = Math.floor(rect.height * dpr)
    canvas.style.width = rect.width + 'px'
    canvas.style.height = rect.height + 'px'
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
    ctx.clearRect(0, 0, rect.width, rect.height)

    canvas.style.color = 'var(--primary)'
    const style = getComputedStyle(canvas)
    ctx.font = style.fontSize + ' ' + style.fontFamily
    ctx.fillStyle = style.color
    ctx.globalAlpha = settings.alpha
    ctx.textBaseline = 'top'

    let queue = []
    function nextToken() {
      while (queue.length === 0) queue = stmt()
      return queue.shift()
    }

    let x = 0
    let y = 0

    while (y < rect.height) {
      const t = nextToken()
      const w = ctx.measureText(t).width
      if (x + w > rect.width) {
        x = 0
        y += settings.lineHeight
        if (y >= rect.height) break
      }
      ctx.fillText(t, x, y)
      x += w + settings.space
    }
  }

  draw()
  window.addEventListener('resize', draw)
})
</script>

The whole calculus fits in six combinators (`arr`, `>>>`, `first`,
`choice`, `loop`, `app`). Everything else (programs, laws, coherence,
graded effects) is built from these as **data**:
`parse >>> validate >>> exec` is a structure you can inspect, rewrite, and
serialize, not a closure you can only call. See
[the paradigm](/paradigm/) for what this buys you.

## The story

Most languages hide their foundations. You apply functions, effects stay
implicit, and the interesting structure (the laws, the rewrites, the
effects) remains locked inside closures nobody can inspect.

Handl starts from the opposite choice: computation as arrows, not
functions. Category theory spent decades building the mathematics for
exactly this: arrows, effects, and handlers, where structure is
first-class and meaning comes from interpretation rather than a hardcoded
runtime. We made that mathematics the IR itself, so programs, laws, and
transformations are all data you can read, rewrite, and execute.

[Read the full story](/story/): from Moggi's monads to Sanada's handlers,
and where Handl picks up.

## The strategy

**handl-lang** is language infrastructure, not a single language: a closed
arrow calculus at the bottom, with engines, runtime-agnostic libraries,
curated kits, tools, and hosts built on top. Composition over application,
inspectable structure over hidden closures.

[The strategy](/strategy/): vision, mission, values, and where it leads.

## The team

A small team building open infrastructure for a new paradigm.

- [Members](/members/): who's building Handl.
- [Contact](/contact/): reach the team directly.

## Get in touch

Handl is open source and very much a work in progress. Questions,
contributions, or just want to see what we're building? The team is small
and easy to reach.

[Contact us →](/contact/) · [GitHub org](https://github.com/handl-lang)
