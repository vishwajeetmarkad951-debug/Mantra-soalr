 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
index df5284426906cdc88098c43365c2b222d09a291f..6a607311e820b7615de1d2222e566edcfb00314f 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,30 @@
-# Mantra-solar
-Solar websites 
+# Mantra Solar
+
+Single-file Marathi landing page for Mantra Solar. The complete website is now inside `index.html`, including HTML, CSS, and JavaScript for easier development and direct Cloudflare Pages deployment.
+
+## Run locally
+
+```bash
+python3 -m http.server 8000
+```
+
+Then open `http://localhost:8000`.
+
+## Development
+
+Edit only `index.html` for normal content, design, and calculator changes:
+
+- Page content and sections are in the `<body>`.
+- UI/UX styles are in the `<style>` block in the `<head>`.
+- Mobile menu and solar calculator logic are in the `<script>` block before `</body>`.
+
+## Cloudflare Pages deployment
+
+Use these settings when deploying this repository to Cloudflare Pages:
+
+- **Framework preset:** None / Static HTML
+- **Build command:** Leave empty
+- **Build output directory:** `/` (repository root)
+- **Production branch:** the branch that contains `index.html`
+
+After deployment, open `https://mantrasolar.in/` to confirm the single-file page is published. If the home page is not visible, purge the Cloudflare cache and redeploy the latest commit.
 
EOF
)
