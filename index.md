---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "handl-lang"
  text: "A new paradigm"
  tagline: "Products and services built on a categorical language — arrows, not functions."
  actions:
    - theme: brand
      text: Products
      link: /handl/
    - theme: brand
      text: Research
      link: /graphopt/
    - theme: alt
      text: The kernel paper
      link: /handl/PAPER

features:
  - title: The paradigm
    details: A categorical language — computation described as arrows, not applied as functions. Structure is inspectable; meaning is supplied by handlers.
    link: /handl/comparison
    linkText: Why not functions
  - title: Handl Language
    details: The platform — a closed arrow-calculus kernel, a data-driven engine, and a plugin-composed host.
    link: /handl/
    linkText: Explore the product
  - title: graphopt
    details: Our first practical product applying Handl Language — a categorical optimizer that mints its own rewrite laws, certifies them, and learns to play the game they create.
    link: /graphopt/
    linkText: Explore the research
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

  const randInt = (min, max) => min + Math.floor(Math.random() * (max - min + 1))
  const pick = (arr) => arr[Math.floor(Math.random() * arr.length)]

  // The kernel vocabulary — the six closed combinators and the
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

## The mission

**handl-lang** builds products and services on a categorical language —
a different paradigm from functional programming. Composition, not
application; structure you can inspect, not closures you can't. The same
foundation drives the language platform and the research stack.
