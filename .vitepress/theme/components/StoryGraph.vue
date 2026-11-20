<script setup>
import { ref } from "vue";
import { VueFlow, MarkerType, Handle, Position } from "@vue-flow/core";
import { Background } from "@vue-flow/background";
import { Controls } from "@vue-flow/controls";
import "@vue-flow/core/dist/style.css";
import "@vue-flow/core/dist/theme-default.css";
import "@vue-flow/controls/dist/style.css";

// Research lineage: two branches (Paterson's syntax-sugar lane above,
// the Prof categorical lane below) converge through Sanada's effects
// work into the Handl node on the right.
const nodes = [
  {
    id: "moggi",
    type: "story",
    position: { x: 0, y: 200 },
    data: {
      year: "1991",
      title: "Monads as notions of computation",
      desc: "Moggi's Notions of Computation and Monads gave denotational semantics a clean algebraic account of effects: a monad is a notion of computation. Wadler then showed monads could structure real functional programs, and the monadic style was born.",
      href: "https://doi.org/10.1016/0890-5401(91)90052-4",
      linkText: "Moggi, Notions of Computation and Monads",
    },
  },
  {
    id: "freyd",
    type: "story",
    position: { x: 0, y: 110 },
    data: {
      year: "late 1990s",
      title: "Freyd & premonoidal categories",
      desc: "While monads took over Haskell, category theorists built the more general setting. Power & Robinson introduced premonoidal categories for notions of computation, and Power & Thielecke developed closed Freyd- and kappa-categories. These models separate pure values from effectful computation, the canonical categorical setting arrows would later inhabit. Levy's Call-by-push-value refined the value/computation discipline they rely on.",
      href: "https://doi.org/10.1017/S0960129597002375",
      linkText: "Power & Robinson, Premonoidal categories",
    },
  },
  {
    id: "hughes",
    type: "story",
    position: { x: 240, y: 200 },
    data: {
      year: "2000",
      title: "Arrows",
      desc: "Monads are great, but some computations do not fit the monadic interface: parsers that need lookahead, GUI code that needs choice, processes that need feedback. Hughes's answer was arrows: a generalization of monads with two type parameters, supporting arr, >>>, first, &&&, |||, loop, and application. He showed how monadic programming techniques generalize and gave three non-monadic libraries that fit naturally.",
      href: "https://doi.org/10.1016/S0167-6423(99)00023-4",
      linkText: "Hughes, Generalising monads to arrows",
    },
  },
  {
    id: "paterson",
    type: "story",
    position: { x: 480, y: 60 },
    data: {
      year: "2001",
      title: "Arrow notation in Haskell",
      desc: "Paterson gave arrows a usable surface syntax. His proc arrow notation made arrows comfortable to program with, implemented as syntax over ordinary functional code: arrow expressions desugar to Haskell functions, and the arrow laws hold up to the host language's semantics. Arrows in Haskell were, and remain, sugar; the real thing lives in the categorical semantics underneath.",
      href: "https://doi.org/10.1145/507635.507664",
      linkText: "Paterson, A new notation for arrows",
    },
  },
  {
    id: "lwy",
    type: "story",
    position: { x: 480, y: 200 },
    data: {
      year: "2010",
      title: "The arrow calculus",
      desc: "Lindley, Wadler & Yallop distilled arrows into a small formal calculus: four constructs, five laws, sound and complete. This is the calculus Handl's kernel is based on.",
      href: "https://doi.org/10.1017/S095679680999027X",
      linkText: "Lindley, Wadler & Yallop, The arrow calculus",
    },
  },
  {
    id: "prof",
    type: "story",
    position: { x: 480, y: 340 },
    data: {
      year: "2006-2010",
      title: "Arrows are strong monads in Prof",
      desc: "A parallel categorical thread asked what arrows really are. Heunen & Jacobs showed arrows are monoids in categories of bifunctors; Jacobs, Heunen & Hasuo built Eilenberg-Moore and Kleisli constructions for them, arrows are Freyd categories; and Asada proved the capstone: arrows are strong monads (promonads) in Prof, where first is exactly strength. The arrow got a canonical semantics.",
      href: "https://doi.org/10.1145/1863597.1863607",
      linkText: "Asada, Arrows are strong monads",
    },
  },
  {
    id: "sanada24",
    type: "story",
    position: { x: 720, y: 200 },
    data: {
      year: "2024",
      title: "Effects & handlers for arrows",
      desc: "Takahiro Sanada extended the arrow calculus with algebraic effects and handlers, interpreted as homomorphisms of algebras over strong promonads.",
      href: "https://doi.org/10.1017/S0956796824000066",
      linkText: "Sanada, Effects and handlers for arrows",
    },
  },
  {
    id: "sanada26",
    type: "story",
    position: { x: 960, y: 200 },
    data: {
      year: "2026",
      title: "Reverse handlers & backpropagation",
      desc: "Sanada, Hoshino, Hirai & Katsumata introduced reverse handlers and modeled neural networks and backpropagation categorically: arrows turned out to be expressive enough to host modern ML.",
      href: "https://doi.org/10.1145/3828704",
      linkText: "Sanada, Hoshino, Hirai & Katsumata, Reverse handlers",
    },
  },
  {
    id: "handl",
    type: "story",
    position: { x: 1200, y: 200 },
    data: {
      year: "",
      title: "Handl",
      final: true,
      desc: "The arrow calculus is not syntax over something else; it is the IR. Programs are 1-morphisms, laws and rewrites are 2-morphisms, and transformations are data like everything else, giving inspectable computation, language as data, graded effects, and interchangeable engines.",
    },
  },
];

const edges = [
  { id: "moggi-hughes", source: "moggi", target: "hughes" },
  { id: "freyd-hughes", source: "freyd", target: "hughes" },
  { id: "hughes-paterson", source: "hughes", target: "paterson" },
  { id: "hughes-lwy", source: "hughes", target: "lwy" },
  {
    id: "lwy-prof",
    source: "lwy",
    target: "prof",
    sourceHandle: "s-bot",
    targetHandle: "t-top",
  },
  { id: "lwy-sanada24", source: "lwy", target: "sanada24" },
  { id: "prof-sanada24", source: "prof", target: "sanada24" },
  { id: "sanada24-sanada26", source: "sanada24", target: "sanada26" },
  { id: "sanada26-handl", source: "sanada26", target: "handl" },
  // Branches converge into Handl on dedicated corridors: Paterson drops
  // in from the top lane, Prof rises from the bottom lane.
  {
    id: "paterson-handl",
    source: "paterson",
    target: "handl",
    targetHandle: "t-top",
  },
  {
    id: "prof-handl",
    source: "prof",
    target: "handl",
    targetHandle: "t-bot",
  },
].map((e) => ({
  ...e,
  type: "smoothstep",
  markerEnd: { type: MarkerType.ArrowClosed, color: "var(--vp-c-text-3)" },
  style: { stroke: "var(--vp-c-text-3)", strokeWidth: 1.5 },
}));

const selected = ref(null);

function onNodeClick({ node }) {
  selected.value = node.data;
}

function clearSelection() {
  selected.value = null;
}
</script>

<template>
  <div class="story-graph">
    <VueFlow
      :nodes="nodes"
      :edges="edges"
      :default-edge-options="{ type: 'smoothstep' }"
      fit-view-on-init
      min-zoom="0.3"
      max-zoom="1.8"
      :nodes-connectable="false"
      :nodes-draggable="false"
      :elements-selectable="true"
      class="story-graph-flow"
      @node-click="onNodeClick"
      @pane-click="clearSelection"
    >
      <template #node-story="props">
        <div
          class="story-node"
          :class="{ 'story-node-final': props.data.final }"
        >
          <Handle :position="Position.Target" type="target" class="story-handle" />
          <Handle :position="Position.Source" type="source" class="story-handle" />
          <Handle
            id="s-bot"
            :position="Position.Bottom"
            type="source"
            class="story-handle"
          />
          <Handle
            id="t-top"
            :position="Position.Top"
            type="target"
            class="story-handle"
          />
          <Handle
            id="t-bot"
            :position="Position.Bottom"
            type="target"
            class="story-handle"
          />
          <div v-if="props.data.year" class="story-node-year">
            {{ props.data.year }}
          </div>
          <div class="story-node-title">{{ props.data.title }}</div>
        </div>
      </template>
      <Background :gap="24" :size="1" />
      <Controls :show-interactive="false" />
    </VueFlow>
    <div class="story-detail" aria-live="polite">
      <template v-if="selected">
        <p class="story-detail-title">
          <span v-if="selected.year" class="story-detail-year"
            >{{ selected.year }}</span
          >
          {{ selected.title }}
        </p>
        <p class="story-detail-desc">{{ selected.desc }}</p>
        <a
          v-if="selected.href"
          :href="selected.href"
          target="_blank"
          rel="noopener"
          class="story-detail-link"
          >{{ selected.linkText }} ↗</a
        >
      </template>
      <p v-else class="story-detail-hint">
        Click a node to see what happened in that era.
      </p>
    </div>
  </div>
</template>

<style scoped>
.story-graph {
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  overflow: hidden;
  margin: 1.25rem 0;
}

.story-graph-flow {
  height: 460px;
  background: var(--vp-c-bg);
}

.story-detail {
  border-top: 1px solid var(--vp-c-divider);
  padding: 0.85rem 1.1rem;
  min-height: 3.5rem;
  background: var(--vp-c-bg-soft);
}

.story-detail-title {
  margin: 0 0 0.3rem;
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--vp-c-text-1);
}

.story-detail-year {
  color: var(--vp-c-brand);
  font-weight: 500;
  margin-right: 0.5em;
}

.story-detail-desc {
  margin: 0 0 0.35rem;
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--vp-c-text-2);
}

.story-detail-link {
  font-size: 0.8rem;
}

.story-detail-hint {
  margin: 0;
  font-size: 0.85rem;
  color: var(--vp-c-text-3);
  font-style: italic;
}

.story-node {
  position: relative;
  min-width: 150px;
  max-width: 190px;
  padding: 0.55rem 0.8rem 0.65rem;
  border-radius: 8px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
  font-family: inherit;
}

.story-node-final {
  border: 2px solid var(--vp-c-brand);
  background: color-mix(in srgb, var(--vp-c-brand) 12%, var(--vp-c-bg));
  min-width: 200px;
  max-width: 230px;
  padding: 0.75rem 1rem 0.85rem;
}

.story-node-year {
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--vp-c-brand);
  margin-bottom: 0.15rem;
}

.story-node-title {
  font-size: 0.82rem;
  line-height: 1.3;
  color: var(--vp-c-text-1);
}

.story-node-final .story-node-title {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--vp-c-brand);
}

.story-handle {
  width: 7px;
  height: 7px;
  background: var(--vp-c-text-3);
  border: none;
}

/* Vue Flow default styles target these classes; keep them subtle */
.story-graph-flow :deep(.vue-flow__controls) {
  box-shadow: none;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  overflow: hidden;
}

.story-graph-flow :deep(.vue-flow__controls-button) {
  background: var(--vp-c-bg);
  border-bottom: 1px solid var(--vp-c-divider);
  fill: var(--vp-c-text-2);
}

.story-graph-flow :deep(.vue-flow__controls-button:hover) {
  background: var(--vp-c-bg-soft);
}

.story-graph-flow :deep(.vue-flow__minimap) {
  display: none;
}
</style>
