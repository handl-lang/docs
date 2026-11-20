import { h } from "vue";
import DefaultTheme from "vitepress/theme";
import StoryGraph from "./components/StoryGraph.vue";
import "./style.css";

export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(
      DefaultTheme.Layout,
      null,
      {
        // Full-width WIP disclaimer bar above the nav, on every page.
        // Height must match --vp-layout-top-height in style.css.
        "layout-top": () => {
          const item = (hidden) =>
            h(
              "span",
              { class: "wip-item", "aria-hidden": hidden ? "true" : undefined },
              [
                h("strong", "Work in progress"),
                ": incomplete, unreviewed docs that may be incorrect or subject to change. Some content may be private or internal.",
              ],
            );
          return h("div", { class: "wip-topbar" }, [
            h("div", { class: "wip-track" }, [
              item(false),
              // Duplicate for the mobile marquee loop; hidden on desktop.
              item(true),
            ]),
          ]);
        },
      },
    );
  },
  enhanceApp({ app }) {
    app.component("StoryGraph", StoryGraph);
  },
  // The mlopt product slug flipped /graphopt/ -> /mlopt/ (mlopt repo's
  // docs/site.yaml `site_path`). GitHub Pages has no server-side
  // redirects and VitePress has no redirect config, so old /graphopt/*
  // URLs land on the 404 page — bounce them client-side to the same
  // path under /mlopt/. Runs on every boot including the 404 fallback.
  setup() {
    if (typeof window === "undefined") return;
    const { pathname, search, hash } = window.location;
    const m = pathname.match(/^(.*)\/graphopt(?=\/|$)/);
    if (m) {
      window.location.replace(
        `${m[1]}/mlopt${pathname.slice(m[0].length)}${search}${hash}`,
      );
    }
  },
};
