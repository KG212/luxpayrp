# MyMoney@Lux — Flask App

## ⚠️ MANDATORY RULE — always apply changes to BOTH apps
Every change made to this Flask app **must also be applied** to the Next.js twin app:
- **Next.js app**: `C:\Users\adm01\Documents\GitHub\mymoney-lux-next`
- After applying changes to both, **push the Next.js app to GitHub**:
  ```powershell
  cd C:\Users\adm01\Documents\GitHub\mymoney-lux-next
  git add .
  git commit -m "feat/fix: <same description as Flask change>"
  git push
  ```
- This triggers auto-deploy to: https://ambitious-beach-0192b5703.7.azurestaticapps.net
- No exceptions — UI changes, calculation fixes, new fields, translations — **always both apps**.

## Project overview
Luxembourg financial calculators: salary, parental leave, crèche (CSA).  
Flask + Jinja2, no database, no auth. Served on Azure App Service.

## Key files
| File | Purpose |
|---|---|
| `app.py` | All Flask routes (`/`, `/salary`, `/parental-leave`, `/creche`, `/set-lang`) |
| `salary_calc.py` | **All calculation logic** — salary, parental leave, CSA/crèche |
| `translations.py` | EN/FR translation dict — single source of truth for all UI text |
| `static/styles.css` | All CSS — design system with CSS variables |
| `templates/base.html` | Base layout: fixed header, nav tabs, ad slots, lang switcher |
| `templates/index.html` | Salary calculator form + results |
| `templates/parental_leave.html` | Parental leave form + results |
| `templates/creche.html` | Crèche/CSA form + results |
| `templates/home.html` | Home/landing page |

## Architecture
- Language stored in `session['lang']` (EN default → FR available)
- Language switched via `/set-lang/<lang>` route, redirects back
- All calculations run server-side in `salary_calc.py`
- Forms POST to the same route, result passed to template via `render_template`
- Jinja2 filter `| currency` formats euro amounts (e.g. `€ 4 000,00`)
- `| safe` used for HTML in translations (links, bold text)

## Calculation logic (salary_calc.py)
- **SSM 2026**: €2 703.74/month (update on next Luxembourg index)
- **Social contributions**: maladie 2.80%, maladie espèce 0.25%, pension 8.50%
- **CIS** (crédit d'impôt salarial): €600/year if income < €40k, tapering to 0 at €80k
- **Assurance dépendance**: 1.40% of (gross − €535)
- **Tax brackets**: `TAX_BRACKETS` dict — Classe 1 / 1A / 2
- **Frais de déplacement**: official unités d'éloignement table (Mémorial A 1021, 4.12.2017)
- **CSA barème**: `CSA_BAREME` dict keyed by `(income_cat, n_children)` → 3 tranches

## Translation system
```python
# translations.py structure
TRANSLATIONS = {
    "en": { "key": "English text", ... },
    "fr": { "key": "Texte français", ... },
}
```
- Always add new keys to **both** EN and FR blocks
- Keys with HTML use `| safe` in templates
- Key naming: `page_field` (e.g. `salary_gross`, `creche_title`, `pl_twins`)

## CSS design system (styles.css)
CSS variables: `--brand #1a6b7c`, `--brand-dark`, `--brand-mid`, `--brand-light #e6f4f7`  
Key classes: `.card`, `.form-stack`, `.toggle-row`, `.toggle-row.checked`, `.frais-fields`, `.btn-primary`, `.btn-secondary`, `.highlight` (green table row), `.row-free`, `.row-warn`, `.badge-yn`

## Important decisions made
- **Frais de déplacement**: toggle + manual input (€/month). The helper text links to the official Journal Officiel (Mémorial A 1021) — NOT taxx.lu
- **Ticket Restaurant**: €50.40/month deducted from net if enabled (toggle)
- **Car benefit**: adds to gross for social contributions AND tax base
- **Parental leave**: CAE treated as separate employer. Employer salary only shown for part-time leave types
- **CSA**: state subsidy shown is the **maximum** — actual depends on structure's own rate
- **Crèche structure price**: field to enter actual hourly rate (some crèches charge €8–9/h above the €7 state max)

## Scheduled task (fires 6am April 22 2026)
Two features to add — see the scheduled CronCreate task in the active Claude session:
1. Crèche: hourly structure price field + excess calculation
2. Home page: hero section + 3 feature cards

## Flask app deployment
- Target: **Azure App Service** (Python 3.12, gunicorn)
- Resource group: `rg-mymoney`
- Startup command: `gunicorn app:app`
- The Next.js version is the parallel static project (see below)

## Parallel project
Next.js static version lives at:  
`C:\Users\adm01\Documents\GitHub\mymoney-lux-next`  
GitHub: https://github.com/KG212/my-money  
Live: https://ambitious-beach-0192b5703.7.azurestaticapps.net
