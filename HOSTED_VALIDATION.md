# College Football hosted validation — 2026-10-24

Live dashboard: https://college-football-statistical-research.streamlit.app/

Repository: https://github.com/Pokered03/College-Football-Statistical-Research

This independent public dashboard and free deployment were authorized. Existing sports dashboards and Multi-Sport Value Engine were not changed.

## FBS and FCS separation

The Division dropdown offers FBS and FCS, with no combined option. It filters manual team selectors, scheduled matchups and nearby schedule dates to the selected division. Cross-division matchup selection is excluded. Rankings use separate division populations. Current registry: 138 FBS / 128 FCS teams. Team histories and opponent-quality summaries still include all covered opponents actually faced, including cross-division games; this is disclosed. The baseline model uses those observed schedule connections and a pooled calibration report, not independently calibrated division-specific probability models. Do not interpret separate views as proof of separate model accuracy.

## Data and permissions

The worker was migrated to the publisher's SportsDataverse release store, whose data license is CC BY 4.0. Integrated tags: cfb_team_info, cfb_schedules, espn_cfb_team_box, espn_cfb_pbp. The broader schedule preserves FCS-only games. Data attribution and modification notices are in the UI and notices/SportsDataverse-attribution.md. Original source/trademark rights remain; no logos, paid APIs or Odds API credits are used. Three stored seasons: 2024–2026. Latest source final at testing: October 17, 2026; a successful refresh does not imply real-time results. Advanced inputs have smaller observed samples, especially FCS.

## Independent software and local performance

- All 52 prepared files matched a fresh public clone at 9599c26dc537f000f4422c5dd79dbcce8d4beebc byte for byte.
- The isolated published clone passed 37 applicable tests, six unrelated cases skipped (2.44 seconds). Tests explicitly exercise division switching, same-division manual teams, cross-division schedule exclusion and released-data team classification/schema.
- SQLite integrity and local HTTP health/root checks passed. Database: 19.52 MiB.
- FBS local 64-switch AppTest: cold render 0.526 seconds, switching p95 0.084 seconds, peak process RSS 145.30 MiB.
- FCS local 64-switch AppTest: switching p95 0.084 seconds, peak process RSS 145.89 MiB across the 128-team registry.
- Cached active-season advanced-data worker: 3.83 seconds, peak RSS 243.63 MiB. Both UI and worker resource targets passed locally.

## Initial live checks

- Independent Streamlit Community Cloud deployment uses main/app.py, Python 3.12 and PyArrow 24.0.0.
- FBS Baylor–Kansas comparison rendered division ranks out of 138; switching the dropdown to FCS rendered Stonehill–Long Island University with ranks out of 128.
- FCS manual comparison and neutral venue worked; returning to FBS allowed Tennessee–South Carolina search/comparison. Last 3/5/10 controls and manual spread −3.5 / total 52.5 inputs worked. Unvalidated spread/total confidence remained PASS.
- Historical 2025 summaries rendered and stale retrospective probability was withheld. October 25 returned an empty FBS schedule and division-specific nearby source dates.
- Initial hosted process memory sampled 166.6 MiB, exposed cgroup limit 3072 MiB, container usage about 688.9–701.2 MiB including other processes and file cache. These are initial observations, not sustained-load results.
- A controlled reboot of only this deployment recovered. FBS default and FCS switching worked after restart; post-restart process peak 161.8 MiB. This verifies one ordinary restart, not extended failure recovery.
- Hosted workflow succeeded in 49 seconds: https://github.com/Pokered03/College-Football-Statistical-Research/actions/runs/40122948411 . Live UI picked up worker timestamp 2026-10-24T18:56:20.242485+00:00.

## Statistical validation and limits

Chronological held-out report: 1,165 games, Brier 0.20459 versus constant 0.25, calibration error 0.04507, scoring-margin MAE 14.771 points, total MAE 12.898 points. Simple comparison baselines: margin MAE 16.941, total MAE 13.487. Early/later prior-fit-game buckets: 889 / 276, using fewer than 10 versus 10+ prior fitted games. These are pooled FBS/FCS results and do not establish separate division calibration or profitability. Win estimates remain conditional and gated; separation score is not model reliability. No verified historical market-line evaluation is integrated, so spread/total confidence stays PASS. Injury, lineup, weather and advanced-player effects are not calibrated inputs.

## Updates and remaining work

Daily free refresh: 10:41 UTC (6:41 AM Eastern daylight time / 5:41 AM standard time), subject to GitHub delays and inactivity policies. ENABLE_FREE_REFRESH=true, public standard ubuntu-latest runner, advanced event processing enabled, no Actions cache/artifact storage. No real-time final-game settlement is promised.

Remaining: verified current injuries/lineups/weather, more complete FCS event data, division-specific probability calibration, real iPhone/MacBook checks, sustained multi-user load, extended failure recovery and hosted stability testing. N/A remains explicit. The complete professional specification and all-six project are not finished. Reboot only this deployment after imported engine changes; data-only updates use database-revision cache keys.
