import { h } from "vue";
import DefaultTheme from "vitepress/theme";
import "./style.css";

export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {});
  },
  enhanceApp({ _app, _router, _siteData }) {
    // app-specific logic
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
