# Sources, permissions and coverage

Primary integrated source: [cfbfastR / SportsDataverse](https://github.com/sportsdataverse/cfbfastR-cfb-data).

The worker reads the SportsDataverse release store, whose data are published under CC BY 4.0. Source attribution and modification notice are preserved in notices/SportsDataverse-attribution.md. Software wrapper licensing is not used as a substitute for the data license.

Release-store source: https://github.com/sportsdataverse/sportsdataverse-data

Integrated tags: cfb_team_info (FBS/FCS membership), cfb_schedules (full schedule), espn_cfb_team_box and espn_cfb_pbp (observed statistics). The narrower ESPN schedule mirror is not substituted for the full FCS calendar. No paid API, credentials or Odds API credits are used. Logos are omitted.

## Snapshot coverage at build time

```json
[
  {
    "season": 2024,
    "teams_with_completed_games": 263,
    "registered_teams": 263,
    "schedule_games": 1612,
    "latest_final": "2025-01-20"
  },
  {
    "season": 2025,
    "teams_with_completed_games": 265,
    "registered_teams": 265,
    "schedule_games": 1625,
    "latest_final": "2026-01-19"
  },
  {
    "season": 2026,
    "teams_with_completed_games": 266,
    "registered_teams": 266,
    "schedule_games": 1539,
    "latest_final": "2026-10-17"
  }
]
```

These counts describe source observations, not independently certified official membership completeness. See the live coverage table for later updates.

## Expanded integrations and remaining gaps

Published play-by-play now supplies observed EPA, positive-EPA success, team passer rating, explosive-play rates, observed red-zone drives, sacks, halftime points/EPA and a source rushing-line-yard proxy where covered. A game must have an observed final-half ending matching the published final score; incomplete histories are excluded. Recorded hurry/sack disruption is explicitly distinguished from tracking pressure. Coverage remains uneven for FCS, and proprietary line grades are not approximated.

## FBS and FCS separation

A mandatory Division dropdown limits the team selectors, scheduled matchup list and nearby schedule dates to FBS or FCS. Cross-division matchups are omitted from these lists. Rankings use separate division populations. Historical opponent-quality summaries describe all covered FBS/FCS opponents actually faced; cross-division games are not silently discarded from team history. The baseline attack/defense fit can use those observed connections; it is not a separately calibrated FBS-versus-FCS prediction. Cross-division confidence is suppressed.

Daily refresh: 10:41 UTC (6:41 AM Eastern daylight time / 5:41 AM standard time), subject to GitHub scheduling delays. Source retrieval and latest completed-game dates are shown separately. Reliable current injury, lineup and weather integrations remain unavailable.
